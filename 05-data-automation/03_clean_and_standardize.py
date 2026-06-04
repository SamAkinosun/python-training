"""Step 3: Clean and standardise the combined readings.

Turns the raw combined file into a tidy dataset that downstream steps can trust:

- drop exact duplicate rows
- standardise clinic names (consistent capitalisation and spacing)
- make the value column numeric and drop rows with missing values
- convert any Fahrenheit temperatures to Celsius so every temp_c row shares one unit

Run:  python 03_clean_and_standardize.py
"""
import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(BASE, "data", "combined_readings.csv")
OUTPUT = os.path.join(BASE, "data", "clean_readings.csv")


def clean():
    if not os.path.exists(INPUT):
        print("combined_readings.csv not found. Run 01_combine_csvs.py first.")
        return None

    df = pd.read_csv(INPUT)
    start_rows = len(df)

    # 1. Remove exact duplicate rows.
    df = df.drop_duplicates()

    # 2. Standardise clinic names: trim spaces and use consistent title case.
    df["clinic"] = df["clinic"].str.strip().str.title()

    # 3. Make values numeric and drop rows where that failed or was blank.
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])

    # 4. Convert Fahrenheit temperatures to Celsius.
    is_fahrenheit = (df["metric"] == "temp_c") & (df["unit"] == "F")
    df.loc[is_fahrenheit, "value"] = ((df.loc[is_fahrenheit, "value"] - 32) * 5 / 9).round(1)
    df.loc[is_fahrenheit, "unit"] = "C"

    df.to_csv(OUTPUT, index=False)
    print(f"Cleaned {start_rows} rows down to {len(df)} -> clean_readings.csv")
    print(f"  duplicates and missing/invalid values removed: {start_rows - len(df)}")
    print(f"  Fahrenheit temperatures converted to Celsius: {int(is_fahrenheit.sum())}")
    return df


if __name__ == "__main__":
    clean()
