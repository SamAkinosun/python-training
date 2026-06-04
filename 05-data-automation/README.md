# Stage 5: Data Automation

Where the earlier stages live in notebooks, real automation lives in **scripts**: small
programs you run from the command line and, eventually, on a schedule with no one watching.
This stage is a set of simple, single-purpose scripts that together form a realistic data
pipeline for a med-tech company.

## The scenario

A medical-device company receives a CSV export of device readings from each clinic every
day (heart rate, SpO2, temperature, systolic blood pressure). The job is to consolidate
those daily files, check the data, clean it, summarise it, and file the originals away,
the same way every day, automatically.

## Important: the data is synthetic

`generate_sample_data.py` produces **made-up** data with a fixed random seed. Patients are
opaque codes like `P0001`; there are no real patients, clinics, devices, or any protected
health information anywhere in this stage. **Never place real patient data in this folder.**

## The scripts (run them in order)

| Script | What it does |
|--------|--------------|
| `generate_sample_data.py` | Creates the daily input files in `data/incoming/` (run this first) |
| `01_combine_csvs.py` | Stacks every daily CSV into one `combined_readings.csv` |
| `02_validate_readings.py` | Flags missing values and out-of-range readings into a quality report |
| `03_clean_and_standardize.py` | Drops duplicates, fixes clinic names and types, converts F to C |
| `04_daily_summary_report.py` | Summarises by day, clinic, and metric into a report |
| `05_archive_files.py` | Moves the processed input files into a dated archive folder |
| `run_pipeline.py` | Runs steps 1 to 5 in order with a single command |

## How to run it

```
cd 05-data-automation
python generate_sample_data.py     # create a batch of daily files
python run_pipeline.py             # combine -> validate -> clean -> summarise -> archive
```

Each script can also be run on its own, in order. Outputs land in `data/` (combined and
clean datasets) and `data/reports/` (the validation and summary reports). That `data/`
folder is not committed to git; recreate it any time by running `generate_sample_data.py`.

## Running it automatically

The point of a pipeline is to run unattended. Once `run_pipeline.py` works, a scheduler can
run it for you:

- **Mac / Linux:** add a line to `crontab -e`, for example to run every weekday at 7am:
  `0 7 * * 1-5 /usr/bin/python3 /full/path/to/run_pipeline.py`
- **Windows:** use Task Scheduler to run `python run_pipeline.py` on a daily trigger.

## What to take away

- Automation scripts do one clear job and can be run from the command line.
- A pipeline chains those steps so the whole job runs with one command.
- Always validate data before trusting it, and archive inputs so they are processed once.
- A scheduler turns "one command" into "runs itself every day".
