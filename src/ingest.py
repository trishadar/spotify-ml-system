import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import pandas as pd

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-recently-played user-library-read"
))

# Pull your last 50 played tracks
results = sp.current_user_recently_played(limit=50)

# Parse tracks
tracks = []
for item in results['items']:
    track = item['track']
    tracks.append({
        "track_id": track["id"],
        "name": track["name"],
        "artist": track["artists"][0]["name"],
        "artist_id": track["artists"][0]["id"],
        "album": track["album"]["name"],
        "played_at": item["played_at"]
    })

# Save to CSV
df = pd.DataFrame(tracks)
df.to_csv("data/raw/recently_played.csv", index=False)

print(f"Saved {len(df)} tracks to data/raw/recently_played.csv")
