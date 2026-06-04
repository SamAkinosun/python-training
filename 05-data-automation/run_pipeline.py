"""Run the whole automation pipeline in order.

This is the heart of automation: instead of running five scripts by hand every day, one
command runs them all in sequence. A scheduler (cron on Mac/Linux, Task Scheduler on
Windows) can then run this one file on a timetable, with no human involved.

Steps, in order:
  1. combine the daily files
  2. validate and write a data-quality report
  3. clean and standardise
  4. build the daily summary report
  5. archive the processed input files

Run:  python run_pipeline.py
"""
import os
import sys
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))

STEPS = [
    "01_combine_csvs.py",
    "02_validate_readings.py",
    "03_clean_and_standardize.py",
    "04_daily_summary_report.py",
    "05_archive_files.py",
]


def run():
    for step in STEPS:
        # flush=True so these headers appear before each script's own output.
        print("\n" + "=" * 70, flush=True)
        print(f"STEP: {step}", flush=True)
        print("=" * 70, flush=True)
        # Run each script with the same Python interpreter; stop if one fails.
        result = subprocess.run([sys.executable, os.path.join(BASE, step)])
        if result.returncode != 0:
            print(f"\nPipeline stopped: {step} exited with an error.")
            return
    print("\nPipeline finished. See data/reports/ for the outputs.")


if __name__ == "__main__":
    run()
