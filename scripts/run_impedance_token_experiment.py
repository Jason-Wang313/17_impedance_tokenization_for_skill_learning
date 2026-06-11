import csv
import math
import os
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULTS = os.path.join(ROOT, "results")
FIGURES = os.path.join(ROOT, "figures")


@dataclass
class Env:
    stiffness: float
    friction: float
    offset: float
    noise: float


@dataclass
class Metrics:
    method: str
    stiffness: float
    friction: float
    offset: float
    seed: int
    mean_abs_force_error: float
    rms_force_error: float
    max_force: float
    safety_violation_rate: float
    contact_loss_rate: float
    tangential_distance: float
    injected_energy: float
    final_force: float


DT = 0.01
HORIZON = 3.0
N_STEPS = int(HORIZON / DT)
TRAIN_STIFFNESS = 100.0
TARGET_FORCE = 8.0
SAFETY_FORCE = 18.0
LOSS_FORCE = 2.0
WIPE_START = 0.55
WIPE_END = 2.55
TAU = 0.075


def phase_at(t):
    if t < WIPE_START:
        return "approach"
    if t < WIPE_END:
        return "wipe"
    return "release"


def smoothstep(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3.0 - 2.0 * x)


def kinematic_policy(t, force, p_cmd):
    train_penetration = TARGET_FORCE / TRAIN_STIFFNESS
    if t < WIPE_START:
        target = train_penetration * smoothstep(t / WIPE_START)
        vt = 0.0
    elif t < WIPE_END:
        target = train_penetration
        vt = 0.20
    else:
        target = train_penetration * (1.0 - smoothstep((t - WIPE_END) / (HORIZON - WIPE_END)))
        vt = 0.0
    return target, vt, 0.0


def gain_schedule_policy(t, force, p_cmd):
    # A stronger baseline: the token stores a different compliance schedule, but
    # force is still not part of the token denotation.
    target, vt, _ = kinematic_policy(t, force, p_cmd)
    if phase_at(t) == "wipe":
        target *= 0.92
    return target, vt, 0.0


def impedance_token_policy(t, force, p_cmd, energy_remaining):
    if t < WIPE_START:
        desired = TARGET_FORCE * smoothstep(t / WIPE_START)
        vt = 0.0
    elif t < WIPE_END:
        desired = TARGET_FORCE
        vt = 0.20
    else:
        desired = TARGET_FORCE * (1.0 - smoothstep((t - WIPE_END) / (HORIZON - WIPE_END)))
        vt = 0.0

    # The token is a local admittance law: force error directly changes
    # penetration intent. This is the semantic difference from motion chunks.
    admittance = 0.018
    damping = 0.88
    raw_dp = admittance * (desired - force) * DT
    raw_dp *= damping

    injected = max(0.0, force * raw_dp)
    if injected > energy_remaining and injected > 0.0:
        raw_dp *= energy_remaining / injected
        injected = energy_remaining
    next_p_cmd = max(0.0, p_cmd + raw_dp)
    return next_p_cmd, vt, injected


def simulate(method, env, seed):
    rng = np.random.default_rng(seed)
    p = max(0.0, env.offset)
    p_cmd = 0.0
    y = 0.0
    force_hist = []
    err_hist = []
    loss_hist = []
    safety_hist = []
    energy_used = 0.0
    prev_p = p

    for step in range(N_STEPS):
        t = step * DT
        p_dot_est = (p - prev_p) / DT
        prev_p = p
        force = max(0.0, env.stiffness * p + 0.7 * math.sqrt(env.stiffness) * max(0.0, p_dot_est))
        if env.noise > 0.0:
            force = max(0.0, force + rng.normal(0.0, env.noise))

        if method == "kinematic_chunk":
            p_cmd, vt_cmd, injected = kinematic_policy(t, force, p_cmd)
        elif method == "gain_schedule":
            p_cmd, vt_cmd, injected = gain_schedule_policy(t, force, p_cmd)
        elif method == "impedance_token":
            p_cmd, vt_cmd, injected = impedance_token_policy(t, force, p_cmd, 3.0 - energy_used)
        else:
            raise ValueError(method)

        energy_used += injected
        p_cmd = max(0.0, min(0.35, p_cmd))
        plant_noise = rng.normal(0.0, env.noise * 0.00012)
        p += DT * (p_cmd - p) / TAU + plant_noise
        p = max(0.0, p)

        contact_quality = min(1.0, force / TARGET_FORCE)
        excess_friction = max(0.0, force - TARGET_FORCE) * env.friction
        vt = vt_cmd * contact_quality * math.exp(-excess_friction / 18.0)
        y += DT * vt

        if phase_at(t) == "wipe":
            force_hist.append(force)
            err_hist.append(force - TARGET_FORCE)
            loss_hist.append(1.0 if force < LOSS_FORCE else 0.0)
            safety_hist.append(1.0 if force > SAFETY_FORCE else 0.0)

    force_arr = np.array(force_hist, dtype=float)
    err_arr = np.array(err_hist, dtype=float)
    loss_arr = np.array(loss_hist, dtype=float)
    safety_arr = np.array(safety_hist, dtype=float)
    return Metrics(
        method=method,
        stiffness=env.stiffness,
        friction=env.friction,
        offset=env.offset,
        seed=seed,
        mean_abs_force_error=float(np.mean(np.abs(err_arr))),
        rms_force_error=float(np.sqrt(np.mean(err_arr ** 2))),
        max_force=float(np.max(force_arr)),
        safety_violation_rate=float(np.mean(safety_arr)),
        contact_loss_rate=float(np.mean(loss_arr)),
        tangential_distance=float(y),
        injected_energy=float(energy_used),
        final_force=float(force_arr[-1]),
    )


def run_grid():
    methods = ["kinematic_chunk", "gain_schedule", "impedance_token"]
    stiffnesses = [35.0, 50.0, 75.0, 100.0, 150.0, 225.0, 325.0, 475.0]
    frictions = [0.10, 0.30, 0.60, 0.95]
    offsets = [-0.010, 0.000, 0.015]
    seeds = list(range(8))
    rows = []
    for method in methods:
        for k in stiffnesses:
            for mu in frictions:
                for offset in offsets:
                    for seed in seeds:
                        env = Env(stiffness=k, friction=mu, offset=offset, noise=0.12)
                        rows.append(simulate(method, env, seed))
    return rows


def write_metrics(rows):
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, "experiment_metrics.csv")
    fields = list(Metrics.__dataclass_fields__.keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: getattr(row, field) for field in fields})
    return path


def aggregate(rows):
    grouped = {}
    for row in rows:
        key = (row.method, row.stiffness)
        grouped.setdefault(key, []).append(row)
    out = []
    for (method, stiffness), vals in sorted(grouped.items()):
        out.append(
            {
                "method": method,
                "stiffness": stiffness,
                "mean_abs_force_error": float(np.mean([v.mean_abs_force_error for v in vals])),
                "rms_force_error": float(np.mean([v.rms_force_error for v in vals])),
                "max_force": float(np.mean([v.max_force for v in vals])),
                "safety_violation_rate": float(np.mean([v.safety_violation_rate for v in vals])),
                "contact_loss_rate": float(np.mean([v.contact_loss_rate for v in vals])),
                "tangential_distance": float(np.mean([v.tangential_distance for v in vals])),
                "injected_energy": float(np.mean([v.injected_energy for v in vals])),
            }
        )
    return out


def write_summary(agg):
    path = os.path.join(RESULTS, "aggregate_by_stiffness.csv")
    fields = [
        "method",
        "stiffness",
        "mean_abs_force_error",
        "rms_force_error",
        "max_force",
        "safety_violation_rate",
        "contact_loss_rate",
        "tangential_distance",
        "injected_energy",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in agg:
            writer.writerow(row)

    by_method = defaultdict_list(agg, "method")
    md = ["# Experiment summary\n"]
    md.append("Grid: 3 methods x 8 stiffness values x 4 friction values x 3 surface offsets x 8 seeds = 2304 runs.\n")
    md.append("| method | mean abs force error | safety violation rate | contact loss rate | tangential distance |")
    md.append("|---|---:|---:|---:|---:|")
    for method, vals in by_method.items():
        md.append(
            "| {} | {:.3f} | {:.3f} | {:.3f} | {:.3f} |".format(
                method,
                np.mean([v["mean_abs_force_error"] for v in vals]),
                np.mean([v["safety_violation_rate"] for v in vals]),
                np.mean([v["contact_loss_rate"] for v in vals]),
                np.mean([v["tangential_distance"] for v in vals]),
            )
        )
    md.append("\nInterpretation: lower force error, safety violation, and contact loss are better; higher tangential distance is better when force remains near target.")
    with open(os.path.join(RESULTS, "experiment_summary.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    return path


def defaultdict_list(rows, key):
    out = {}
    for row in rows:
        out.setdefault(row[key], []).append(row)
    return out


def plot_results(agg):
    os.makedirs(FIGURES, exist_ok=True)
    methods = ["kinematic_chunk", "gain_schedule", "impedance_token"]
    colors = {
        "kinematic_chunk": "#7a3f2a",
        "gain_schedule": "#6a6f1d",
        "impedance_token": "#176f8f",
    }
    labels = {
        "kinematic_chunk": "Kinematic chunks",
        "gain_schedule": "Gain schedule",
        "impedance_token": "Impedance tokens",
    }
    by_method = defaultdict_list(agg, "method")

    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    for method in methods:
        vals = sorted(by_method[method], key=lambda r: r["stiffness"])
        ax.plot(
            [v["stiffness"] for v in vals],
            [v["mean_abs_force_error"] for v in vals],
            marker="o",
            linewidth=2.2,
            color=colors[method],
            label=labels[method],
        )
    ax.axvline(TRAIN_STIFFNESS, color="#444444", linestyle="--", linewidth=1.0)
    ax.set_xlabel("Held-out environment stiffness")
    ax.set_ylabel("Mean absolute force error (N)")
    ax.set_title("Force robustness under contact-parameter shift")
    ax.grid(True, alpha=0.28)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES, "force_error_by_stiffness.pdf"))
    fig.savefig(os.path.join(FIGURES, "force_error_by_stiffness.png"), dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    for method in methods:
        vals = sorted(by_method[method], key=lambda r: r["stiffness"])
        ax.plot(
            [v["stiffness"] for v in vals],
            [v["safety_violation_rate"] for v in vals],
            marker="s",
            linewidth=2.2,
            color=colors[method],
            label=labels[method],
        )
    ax.axvline(TRAIN_STIFFNESS, color="#444444", linestyle="--", linewidth=1.0)
    ax.set_xlabel("Held-out environment stiffness")
    ax.set_ylabel("Safety violation fraction")
    ax.set_title("Over-force events during wiping")
    ax.grid(True, alpha=0.28)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES, "safety_by_stiffness.pdf"))
    fig.savefig(os.path.join(FIGURES, "safety_by_stiffness.png"), dpi=180)
    plt.close(fig)


def write_latex_table(agg):
    by_method = defaultdict_list(agg, "method")
    path = os.path.join(RESULTS, "experiment_table.tex")
    names = {
        "kinematic_chunk": "Kinematic chunks",
        "gain_schedule": "Gain schedule",
        "impedance_token": "Impedance tokens",
    }
    with open(path, "w", encoding="utf-8") as f:
        f.write("\\begin{tabular}{lrrrr}\\toprule\n")
        f.write("Method & Force err. $\\downarrow$ & Safety frac. $\\downarrow$ & Loss frac. $\\downarrow$ & Wipe dist. $\\uparrow$ \\\\\n")
        f.write("\\midrule\n")
        for method in ["kinematic_chunk", "gain_schedule", "impedance_token"]:
            vals = by_method[method]
            f.write(
                "{} & {:.2f} & {:.3f} & {:.3f} & {:.3f} \\\\\n".format(
                    names[method],
                    np.mean([v["mean_abs_force_error"] for v in vals]),
                    np.mean([v["safety_violation_rate"] for v in vals]),
                    np.mean([v["contact_loss_rate"] for v in vals]),
                    np.mean([v["tangential_distance"] for v in vals]),
                )
            )
        f.write("\\bottomrule\n\\end{tabular}\n")
    return path


def main():
    os.makedirs(RESULTS, exist_ok=True)
    os.makedirs(FIGURES, exist_ok=True)
    rows = run_grid()
    metrics_path = write_metrics(rows)
    agg = aggregate(rows)
    summary_path = write_summary(agg)
    table_path = write_latex_table(agg)
    plot_results(agg)
    print(f"wrote {metrics_path}")
    print(f"wrote {summary_path}")
    print(f"wrote {table_path}")
    print("wrote figures/force_error_by_stiffness.pdf and figures/safety_by_stiffness.pdf")


if __name__ == "__main__":
    main()
