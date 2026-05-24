import yfinance as yf
import pandas as pd
from pathlib import Path

TICKER = ""
START_DATE = "2024-01-01"
END_DATE = "2024-12-31"
OUT_FILE = f"{TICKER.lower()}_2024.csv"

# Get data
df = yf.download(TICKER, start=START_DATE, end=END_DATE, auto_adjust=True, progress=False)

# Error with y-finance
if df.empty:
    raise RuntimeError("No data returned. Try again")

# If we get multi-index columns:
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# Keep the only columns we need
df = df[["Open", "High", "Low", "Close", "Volume"]].copy()
df.index.name = "Date"
df = df.dropna()

# Save to csv
out_path = Path(OUT_FILE)
df.to_csv(out_path)