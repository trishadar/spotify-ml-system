import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import pandas as pd

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-library-read playlist-read-private"
))

# Pull saved tracks (limit 50 per request)
saved_tracks = []
offset = 0
while True:
    results = sp.current_user_saved_tracks(limit=50, offset=offset)
    if not results['items']:
        break
    for item in results['items']:
        track = item['track']
        saved_tracks.append({
            "track_id": track['id'],
            "name": track['name'],
            "artist": track['artists'][0]['name'],
            "album": track['album']['name']
        })
    offset += 50

df_saved = pd.DataFrame(saved_tracks)
df_saved.to_csv("data/raw/saved_tracks.csv", index=False)
print(f"Saved {len(df_saved)} saved tracks to data/raw/saved_tracks.csv")
