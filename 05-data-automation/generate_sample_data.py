"""Generate synthetic daily medical-device reading files for the automation lessons.

Creates several daily CSV files under data/incoming/, simulating exports that a med-tech
company might receive from clinics each day. The data is entirely MADE UP with a fixed
random seed:

- Patients are opaque codes (P0001, ...), never real names. There is no real patient,
  clinic, or device information of any kind. Do not put real patient data in this folder.

A few realistic problems are baked in on purpose so the validation and cleaning scripts
have something to find: out-of-range values, missing values, duplicate IDs, temperatures
in Fahrenheit, and inconsistent clinic names.

Run:  python generate_sample_data.py
"""
import os
import csv
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
INCOMING = os.path.join(BASE, "data", "incoming")
os.makedirs(INCOMING, exist_ok=True)

rng = np.random.default_rng(7)

CLINICS = ["Riverside Clinic", "Lakeview Medical", "Summit Health"]
DEVICES = ["D-100", "D-101", "D-102", "D-103", "D-104"]
DAYS = ["2024-03-04", "2024-03-05", "2024-03-06", "2024-03-07", "2024-03-08"]

# metric -> (unit, healthy_low, healthy_high)
METRICS = {
    "heart_rate": ("bpm", 55, 100),
    "spo2": ("%", 95, 100),
    "temp_c": ("C", 36.1, 37.5),
    "bp_systolic": ("mmHg", 100, 140),
}

reading_id = 1
for day in DAYS:
    rows = []
    for _ in range(120):
        clinic = rng.choice(CLINICS)
        # Inconsistent capitalisation on some rows (cleaning will fix this).
        if rng.random() < 0.15:
            clinic = clinic.lower()

        device = rng.choice(DEVICES)
        patient = f"P{rng.integers(1, 51):04d}"
        metric = rng.choice(list(METRICS))
        unit, low, high = METRICS[metric]

        # A normal-ish value within the healthy band.
        value = round(float(rng.uniform(low, high)), 1)

        # Inject some out-of-range values (validation will flag these).
        if rng.random() < 0.04:
            value = round(value * rng.choice([0.3, 2.2]), 1)

        # A few temperatures arrive in Fahrenheit (cleaning will convert these).
        if metric == "temp_c" and rng.random() < 0.2:
            value = round(value * 9 / 5 + 32, 1)
            unit = "F"

        # A few missing values.
        if rng.random() < 0.03:
            value = ""

        rows.append([reading_id, f"{day}T09:00:00", clinic, device, patient,
                     metric, value, unit])
        reading_id += 1

    # Duplicate two rows in each file (cleaning will drop duplicates).
    rows.append(rows[5])
    rows.append(rows[15])

    path = os.path.join(INCOMING, f"readings_{day}.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["reading_id", "timestamp", "clinic", "device_id",
                         "patient_ref", "metric", "value", "unit"])
        writer.writerows(rows)
    print(f"wrote {path} ({len(rows)} rows)")

print("Done. Daily files are in data/incoming/")
