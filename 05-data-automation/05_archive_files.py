"""Step 5: Archive the processed input files.

Once the daily files have been combined and processed, move them out of the incoming folder
into a dated archive folder. This keeps the incoming folder ready for the next batch and
means files are never processed twice.

Run:  python 05_archive_files.py
"""
import os
import glob
import shutil
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
INCOMING = os.path.join(BASE, "data", "incoming")
ARCHIVE = os.path.join(BASE, "data", "archive")


def archive():
    files = sorted(glob.glob(os.path.join(INCOMING, "*.csv")))
    if not files:
        print("Nothing to archive: data/incoming/ is empty.")
        return []

    # A folder named for the run date, e.g. archive/2024-03-08/.
    run_date = datetime.now().strftime("%Y-%m-%d")
    target = os.path.join(ARCHIVE, run_date)
    os.makedirs(target, exist_ok=True)

    moved = []
    for path in files:
        name = os.path.basename(path)
        shutil.move(path, os.path.join(target, name))
        moved.append(name)
        print(f"  archived {name}")

    print(f"Moved {len(moved)} file(s) into archive/{run_date}/")
    print("(Run generate_sample_data.py again to create a fresh batch.)")
    return moved


if __name__ == "__main__":
    archive()
