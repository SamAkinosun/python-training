"""Step 1: Combine many daily CSV exports into one file.

A very common automation task: several files land in a folder and you need them stacked
into a single dataset. This reads every CSV in data/incoming/ and writes one combined file.

Run:  python 01_combine_csvs.py
"""
import os
import glob
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
INCOMING = os.path.join(BASE, "data", "incoming")
OUTPUT = os.path.join(BASE, "data", "combined_readings.csv")


def combine():
    files = sorted(glob.glob(os.path.join(INCOMING, "*.csv")))
    if not files:
        print("No CSV files found in data/incoming/. Run generate_sample_data.py first.")
        return None

    frames = []
    for path in files:
        frames.append(pd.read_csv(path))
        print(f"  read {os.path.basename(path)}")

    combined = pd.concat(frames, ignore_index=True)
    combined.to_csv(OUTPUT, index=False)
    print(f"Combined {len(files)} files into {len(combined)} rows -> {os.path.basename(OUTPUT)}")
    return combined


if __name__ == "__main__":
    combine()
