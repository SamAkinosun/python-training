# Stage 4: Data Science (Financial Analysis)

An applied stage that turns the Python and pandas skills from the earlier stages into a
real analyst workflow, using financial market data as the worked example. The techniques
here (loading, cleaning, grouping, summarising, plotting) are everyday data-analyst skills;
the financial parts (returns, moving averages, volatility, portfolios) show them in action.

Make sure the data libraries are installed (from the project root):

```
pip install -r requirements.txt
```

## The dataset

`data/stock_history.csv` is **synthetic**: three years of daily Open/High/Low/Close/Volume
for four fictional tickers (`ATLAS`, `HELIOS`, `NORTH`, `VERTEX`), produced by
`generate_data.ipynb` with a fixed random seed. It contains no real market, company, or
personal data. Re-create it any time by running `generate_data.ipynb`.

## Lessons

| # | Notebook | You will be able to |
|---|----------|---------------------|
| 1 | `01_data_science_workflow.ipynb` | Describe the analyst workflow and load the dataset |
| 2 | `02_loading_and_inspecting.ipynb` | Inspect a dataset's size, types, and gaps; slice a time series |
| 3 | `03_cleaning_and_preparing.ipynb` | Remove duplicates and handle missing values sensibly |
| 4 | `04_exploring_and_aggregating.ipynb` | Group, pivot, and resample data |
| 5 | `05_financial_returns.ipynb` | Compute daily, cumulative, and log returns |
| 6 | `06_moving_averages_and_trends.ipynb` | Smooth prices and read trend signals |
| 7 | `07_volatility_and_risk.ipynb` | Measure volatility, annualise it, and compute drawdown |
| 8 | `08_portfolio_analysis.ipynb` | Combine assets into a weighted portfolio and study correlation |
| 9 | `09_visualizing_financial_data.ipynb` | Build rebased line charts, histograms, and heatmaps |
| 10 | `10_capstone_portfolio_report.ipynb` | Produce an end-to-end portfolio report |

## Files in this folder

- `generate_data.ipynb` - regenerates the synthetic dataset.
- `data/stock_history.csv` - the generated data used by every lesson.

## How to work through a notebook

Read each section, run the cells, and do the **Practice** before checking the
**Practice Solutions** at the bottom. Finish with the capstone, then try the same report on
a real CSV of your own.
