"""Download and prepare UK Carbon Intensity API data.

The API schema can evolve, so the script keeps the transformation layer
explicit and easy to adapt. Raw data should not be committed to GitHub.
"""

from pathlib import Path
import json
import requests
import pandas as pd

API_URL = "https://api.carbonintensity.org.uk/intensity/date"
OUTPUT = Path("data/carbon_intensity_clean.csv")


def download_json(date: str) -> dict:
    """Download one day's carbon-intensity data (YYYY-MM-DD)."""
    response = requests.get(f"{API_URL}/{date}", timeout=30)
    response.raise_for_status()
    return response.json()


def flatten_intensity(payload: dict) -> pd.DataFrame:
    """Flatten the API response into an analysis-friendly dataframe."""
    rows = []
    for item in payload.get("data", []):
        intensity = item.get("intensity", {})
        rows.append(
            {
                "timestamp": item.get("from"),
                "to": item.get("to"),
                "carbon_intensity": intensity.get("actual"),
                "forecast_intensity": intensity.get("forecast"),
                "index": intensity.get("index"),
            }
        )
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    df["to"] = pd.to_datetime(df["to"], utc=True)
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.day_name()
    df["month"] = df["timestamp"].dt.month
    df["is_weekend"] = df["timestamp"].dt.dayofweek >= 5
    return df


if __name__ == "__main__":
    # Example: replace with the dates you want to analyse.
    dates = ["2026-01-01"]
    frames = []
    for date in dates:
        payload = download_json(date)
        frames.append(flatten_intensity(payload))

    df = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"Saved {len(df):,} rows to {OUTPUT}")
