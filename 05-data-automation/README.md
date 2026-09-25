# Stage 5: Data Automation

Automation means running the same job the same way every time, eventually on a schedule
with no one watching. This stage is a set of simple, single-purpose notebooks that
together form a realistic data pipeline for a med-tech company.

## The scenario

A medical-device company receives a CSV export of device readings from each clinic every
day (heart rate, SpO2, temperature, systolic blood pressure). The job is to consolidate
those daily files, check the data, clean it, summarise it, and file the originals away,
the same way every day, automatically.

## Important: the data is synthetic

`generate_sample_data.ipynb` produces **made-up** data with a fixed random seed. Patients
are opaque codes like `P0001`; there are no real patients, clinics, devices, or any
protected health information anywhere in this stage. **Never place real patient data in
this folder.**

## The notebooks (run them in order)

| Notebook | What it does |
|----------|--------------|
| `generate_sample_data.ipynb` | Creates the daily input files in `data/incoming/` (run this first) |
| `01_combine_csvs.ipynb` | Stacks every daily CSV into one `combined_readings.csv` |
| `02_validate_readings.ipynb` | Flags missing values and out-of-range readings into a quality report |
| `03_clean_and_standardize.ipynb` | Drops duplicates, fixes clinic names and types, converts F to C |
| `04_daily_summary_report.ipynb` | Summarises by day, clinic, and metric into a report |
| `05_archive_files.ipynb` | Moves the processed input files into a dated archive folder |
| `run_pipeline.ipynb` | Runs steps 1 to 5 in order with a single click |

## How to run it

1. Open `generate_sample_data.ipynb` and choose **Run > Run All Cells** to create a batch
   of daily files.
2. Open `run_pipeline.ipynb` and choose **Run > Run All Cells**. It runs combine, validate,
   clean, summarise, and archive in order.

Each step notebook can also be opened and run on its own, in order. Outputs land in
`data/` (combined and clean datasets) and `data/reports/` (the validation and summary
reports). That `data/` folder is not committed to git; recreate it any time by running
`generate_sample_data.ipynb`.

## Running it automatically

The point of a pipeline is to run unattended. A scheduler cannot click Run All, so it uses
`jupyter nbconvert`, which runs a notebook from the terminal and saves a copy of the
finished run in `data/logs/`:

```
cd /full/path/to/05-data-automation
jupyter nbconvert --to notebook --execute --output-dir data/logs run_pipeline.ipynb
```

- **Mac / Linux:** add a line to `crontab -e`, for example to run every weekday at 7am
  (use the full path to `jupyter`, which `which jupyter` prints):
  `0 7 * * 1-5 cd /full/path/to/05-data-automation && /full/path/to/jupyter nbconvert --to notebook --execute --output-dir data/logs run_pipeline.ipynb`
- **Windows:** use Task Scheduler with a daily trigger. Set the program to `jupyter`, the
  arguments to `nbconvert --to notebook --execute --output-dir data\logs run_pipeline.ipynb`,
  and "Start in" to the `05-data-automation` folder.

## What to take away

- Automation steps do one clear job and can be run on their own.
- A pipeline chains those steps so the whole job runs with one command.
- Always validate data before trusting it, and archive inputs so they are processed once.
- A scheduler turns "one command" into "runs itself every day".
