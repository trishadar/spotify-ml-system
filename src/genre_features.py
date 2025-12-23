import pandas as pd
from collections import Counter

tracks = pd.read_csv("data/raw/recently_played.csv")
artists = pd.read_csv("data/processed/artists.csv")

df = tracks.merge(artists, on="artist_id", how="left")

genre_counts = Counter()

for genres in df["genres"].dropna():
    for g in genres.split("|"):
        genre_counts[g] += 1

genre_df = (
    pd.DataFrame.from_dict(genre_counts, orient="index", columns=["count"])
    .sort_values("count", ascending=False)
)

genre_df.to_csv("data/processed/genre_distribution.csv")

print("Top genres:")
print(genre_df.head(10))
