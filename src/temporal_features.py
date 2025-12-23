import pandas as pd

df = pd.read_csv("data/raw/recently_played.csv")
df["played_at"] = pd.to_datetime(df["played_at"])

df["hour"] = df["played_at"].dt.hour
df["weekday"] = df["played_at"].dt.weekday

features = {
    "avg_hour": df["hour"].mean(),
    "weekend_rate": (df["weekday"] >= 5).mean(),
    "night_listening_rate": ((df["hour"] >= 22) | (df["hour"] <= 5)).mean(),
    "unique_artists": df["artist"].nunique(),
    "repeat_rate": 1 - df["track_id"].nunique() / len(df)
}

pd.DataFrame([features]).to_csv(
    "data/processed/user_behavior_features.csv",
    index=False
)

print(features)
