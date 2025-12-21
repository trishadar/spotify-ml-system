import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Debug: make sure they're loaded
print("CLIENT ID:", SPOTIFY_CLIENT_ID)
print("CLIENT SECRET:", SPOTIFY_CLIENT_SECRET)
print("REDIRECT URI:", SPOTIFY_REDIRECT_URI)