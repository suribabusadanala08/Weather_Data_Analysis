import pandas as pd

def monthly_state_summary(df, state):
    subset = df[df["state"].str.casefold() == state.casefold()].copy()
    subset["date"] = pd.to_datetime(subset["date"])
    return subset.groupby(subset["date"].dt.to_period("M"))[
        ["temperature", "humidity", "rainfall", "wind_speed"]
    ].mean().reset_index()
