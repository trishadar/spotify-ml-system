import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="user-read-recently-played"
    )
)

df = pd.read_csv("data/raw/recently_played.csv")

artist_rows = []

for artist_id in df["artist_id"].unique():
    try:
        artist = sp.artist(artist_id)
        artist_rows.append({
            "artist_id": artist_id,
            "artist_name": artist["name"],
            "artist_popularity": artist["popularity"],
            "genres": "|".join(artist["genres"])
        })
    except:
        continue

artists = pd.DataFrame(artist_rows)
artists.to_csv("data/processed/artists.csv", index=False)

print("Saved artists.csv:", artists.shape)
