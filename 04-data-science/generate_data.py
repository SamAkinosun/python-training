"""Generate the synthetic financial dataset used by the data science lessons.

Produces data/stock_history.csv: daily OHLCV (Open, High, Low, Close, Volume) rows for a
handful of FICTIONAL tickers across three years of trading days. The data is made up with
a fixed random seed, so it is reproducible and contains no real market, company, or
personal information.

Run:  python generate_data.py
"""
import os
import numpy as np
import pandas as pd

OUT = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT, exist_ok=True)

# Fixed seed -> the same data every time.
rng = np.random.default_rng(42)

# Trading days (business days) across three years.
dates = pd.bdate_range("2021-01-04", "2023-12-29")

# Fictional tickers, each with its own character:
#   start price, average daily drift, daily volatility.
tickers = {
    "ATLAS":   dict(start=100.0, drift=0.0006, vol=0.018),  # steady grower
    "HELIOS":  dict(start=60.0,  drift=0.0010, vol=0.035),  # high growth, volatile
    "NORTH":   dict(start=240.0, drift=0.0002, vol=0.012),  # slow and stable
    "VERTEX":  dict(start=30.0,  drift=-0.0003, vol=0.028), # gentle decline, choppy
}

rows = []
for ticker, cfg in tickers.items():
    n = len(dates)
    daily_returns = rng.normal(cfg["drift"], cfg["vol"], size=n)
    close = cfg["start"] * np.cumprod(1 + daily_returns)

    prev_close = np.empty(n)
    prev_close[0] = cfg["start"]
    prev_close[1:] = close[:-1]

    open_ = prev_close * (1 + rng.normal(0, 0.004, size=n))
    high = np.maximum(open_, close) * (1 + np.abs(rng.normal(0, 0.006, size=n)))
    low = np.minimum(open_, close) * (1 - np.abs(rng.normal(0, 0.006, size=n)))
    volume = rng.integers(500_000, 5_000_000, size=n)

    for i, d in enumerate(dates):
        rows.append({
            "Date": d.date().isoformat(),
            "Ticker": ticker,
            "Open": round(float(open_[i]), 2),
            "High": round(float(high[i]), 2),
            "Low": round(float(low[i]), 2),
            "Close": round(float(close[i]), 2),
            "Volume": int(volume[i]),
        })

df = pd.DataFrame(rows)
# Inject a few realistic blemishes for the cleaning lesson:
# a handful of missing Close values and two duplicated rows.
blemish = df.sample(8, random_state=1).index
df.loc[blemish, "Close"] = np.nan
df = pd.concat([df, df.iloc[[10, 20]]], ignore_index=True)

path = os.path.join(OUT, "stock_history.csv")
df.to_csv(path, index=False)
print(f"wrote {path}: {len(df)} rows, tickers={list(tickers)}")
