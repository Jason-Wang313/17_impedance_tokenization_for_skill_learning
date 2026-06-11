import csv
import os


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MATRIX = os.path.join(ROOT, "docs", "related_work_matrix.csv")


PATTERNS = [
    "Variable Impedance Control and Learning",
    "A survey of robot manipulation in contact",
    "Dynamic movement primitives in robotics",
    "Efficient Force Control Learning System",
    "Robot learning from demonstration of force-based manipulation",
    "Learning Fine-Grained Bimanual Manipulation",
    "Reactive Diffusion Policy",
    "Modeling robot discrete movements with state-varying stiffness",
    "A Survey on Imitation Learning for Contact-Rich Tasks",
    "Robot Learning from Demonstration in Robotic Assembly",
]


def main():
    with open(MATRIX, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for pattern in PATTERNS:
        lower = pattern.lower()
        match = None
        for row in rows:
            if lower in row.get("title", "").lower():
                match = row
                break
        print(f"PATTERN: {pattern}")
        if not match:
            print("  NOT FOUND")
            continue
        for key in ["rank", "title", "year", "authors", "source", "doi", "url", "cited_by_count"]:
            print(f"  {key}: {match.get(key, '')}")
        print()


if __name__ == "__main__":
    main()
