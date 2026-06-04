"""Step 4: Build a daily summary report from the clean readings.

Most automations end by producing something a person actually reads. This summarises the
clean data by day, clinic, and metric (count, average, minimum, maximum) and writes it to a
report file, then prints a short headline summary to the screen.

Run:  python 04_daily_summary_report.py
"""
import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(BASE, "data", "clean_readings.csv")
REPORTS = os.path.join(BASE, "data", "reports")
REPORT = os.path.join(REPORTS, "daily_summary.csv")


def summarise():
    if not os.path.exists(INPUT):
        print("clean_readings.csv not found. Run 03_clean_and_standardize.py first.")
        return None

    df = pd.read_csv(INPUT)
    os.makedirs(REPORTS, exist_ok=True)

    # The date is the part of the timestamp before the 'T'.
    df["date"] = df["timestamp"].str.split("T").str[0]

    summary = (
        df.groupby(["date", "clinic", "metric"])["value"]
          .agg(["count", "mean", "min", "max"])
          .round(1)
          .reset_index()
    )
    summary.to_csv(REPORT, index=False)

    print(f"Wrote {len(summary)} summary rows -> reports/daily_summary.csv")
    print(f"  dates covered: {df['date'].min()} to {df['date'].max()}")
    print(f"  clinics: {', '.join(sorted(df['clinic'].unique()))}")
    print("  average value per metric (whole period):")
    for metric, mean in df.groupby("metric")["value"].mean().round(1).items():
        print(f"    {metric:12s} {mean}")
    return summary


if __name__ == "__main__":
    summarise()
