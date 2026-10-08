from pathlib import Path
import pandas as pd

INPUT = Path("data/carbon_intensity_clean.csv")


def analyse(df: pd.DataFrame) -> None:
    required = {"timestamp", "carbon_intensity", "hour", "day_of_week", "is_weekend"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    print("Rows:", len(df))
    print("Missing values:\n", df.isna().sum())
    print("\nSummary:\n", df["carbon_intensity"].describe())

    hourly = (
        df.groupby("hour", as_index=False)["carbon_intensity"]
        .mean()
        .sort_values("carbon_intensity", ascending=False)
    )
    print("\nAverage carbon intensity by hour:\n", hourly)

    weekend = df.groupby("is_weekend")["carbon_intensity"].mean()
    print("\nWeekday/weekend average carbon intensity:\n", weekend)


if __name__ == "__main__":
    if not INPUT.exists():
        raise FileNotFoundError(
            f"{INPUT} not found. Run 01_data_ingestion_cleaning.py first."
        )
    data = pd.read_csv(INPUT, parse_dates=["timestamp", "to"])
    analyse(data)
