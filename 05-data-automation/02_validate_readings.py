"""Step 2: Validate the combined readings and write a data-quality report.

Automation is not just moving data around; it is also checking that the data is sane before
anyone relies on it. This flags two kinds of problem and writes them to a report:

- missing or non-numeric values
- values outside a plausible clinical range for their metric

Temperatures recorded in Fahrenheit are converted to Celsius before the range check, so a
unit difference is not mistaken for a bad value.

Run:  python 02_validate_readings.py
"""
import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(BASE, "data", "combined_readings.csv")
REPORTS = os.path.join(BASE, "data", "reports")
REPORT = os.path.join(REPORTS, "validation_report.csv")

# Plausible range for each metric, in its canonical unit.
RANGES = {
    "heart_rate": (30, 200),
    "spo2": (70, 100),
    "temp_c": (30, 43),
    "bp_systolic": (70, 220),
}


def to_celsius(value, unit):
    if unit == "F":
        return (value - 32) * 5 / 9
    return value


def validate():
    if not os.path.exists(INPUT):
        print("combined_readings.csv not found. Run 01_combine_csvs.py first.")
        return None

    df = pd.read_csv(INPUT)
    os.makedirs(REPORTS, exist_ok=True)

    # Numeric version of value; anything that cannot convert becomes NaN.
    numeric = pd.to_numeric(df["value"], errors="coerce")

    problems = []
    for i, row in df.iterrows():
        value = numeric[i]

        if pd.isna(value):
            problems.append({**row.to_dict(), "issue": "missing or non-numeric value"})
            continue

        low, high = RANGES.get(row["metric"], (None, None))
        if low is None:
            problems.append({**row.to_dict(), "issue": f"unknown metric '{row['metric']}'"})
            continue

        checked = to_celsius(value, row["unit"]) if row["metric"] == "temp_c" else value
        if checked < low or checked > high:
            problems.append({**row.to_dict(), "issue": f"out of range ({low}-{high})"})

    report = pd.DataFrame(problems)
    report.to_csv(REPORT, index=False)

    print(f"Checked {len(df)} rows. Found {len(report)} problem rows -> reports/validation_report.csv")
    if not report.empty:
        print("Breakdown by issue:")
        for issue, count in report["issue"].value_counts().items():
            print(f"  {count:4d}  {issue}")
    return report


if __name__ == "__main__":
    validate()
