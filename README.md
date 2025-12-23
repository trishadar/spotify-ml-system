# Spotify Song Recommendation System

Predict which songs a user is likely to enjoy based on their Spotify listening history.

## Overview

This project builds a machine learning system that analyzes your Spotify listening habits using metadata like artist, genre, and temporal listening patterns. It predicts whether a user would like a song, without relying on restricted audio features from the Spotify API.

## Project Structure

data/
├─ raw/ # Saved tracks CSV
├─ processed/ # Processed tracks with artist, genre, and temporal info
src/
├─ ingest.py
├─ enrich_artists.py
├─ genre_features.py
├─ train_model.py
├─ predict.py
├─ visualize_taste.py


## Setup

```bash
pip install spotipy pandas matplotlib seaborn scikit-learn
```
Configure Spotify API credentials in config.py:
```python
SPOTIFY_CLIENT_ID = "your_client_id"
SPOTIFY_CLIENT_SECRET = "your_client_secret"
SPOTIFY_REDIRECT_URI = "your_redirect_uri"
```

Ensure directories exist:
```bash
mkdir -p data/raw data/processed assets/visualizations
```

## Usage

# Extract your recently played tracks
python src/ingest.py

# Enrich track data with artist and genre info
python src/enrich_artists.py
python src/genre_features.py

# Train the ML model
python src/train_model.py

# Predict song likes
python src/predict.py

# Visualize listening patterns
python src/visualize_taste.py

## Visualization

![Top Genres](assets/visualizations/genre_distribution.png)

## Notes

- Model is trained on user metadata (artist, genre, listening time).
- Only public and available tracks are processed.
- seaborn is optional for nicer visualizations.