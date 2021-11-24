import json
import lyricsgenius
import os
import spotipy

from dotenv import load_dotenv
from models import *
from peewee import *
from rich import print
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm

# Load environment variables
load_dotenv()

# Setup database
database_path = os.path.join(os.path.dirname(__file__), "../data/database.db")

db.init(database_path)
db.create_tables([
    Album,
    AlbumTrack,
    Artist,
    Genre,
    Track,
    Track.artists.get_through_model(),
    Album.artists.get_through_model(),
    Artist.genres.get_through_model()
])

# Create Spotify connection
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/redirect",
))

f = open(os.path.join(os.path.dirname(__file__), "../data/dataset.json"))

playlists = json.load(f)["playlists"]

# Iterate over playlist
for playlist in tqdm(playlists):
    playlist_track_uris = []

    for playlist_track in playlist["tracks"]:
        playlist_track_uris.append(playlist_track["track_uri"].split(":")[2])

    for i in range(0, len(playlist_track_uris), 50):
        track_uris = playlist_track_uris[i:i + 50]
        tracks = sp.tracks(track_uris)["tracks"]

        for track in tracks:
            album_data = track["album"]

            # Save album
            album_instance, album_created = Album.get_or_create(
                uri=album_data["uri"],
                name=album_data["name"],
                album_type=album_data["album_type"],
                release_date=album_data["release_date"],
                total_tracks=album_data["total_tracks"]
            )

            album_artists_ids = []

            # Save album artists
            if album_created:
                for artist_data in album_data["artists"]:
                    artist = sp.artist(artist_data["uri"])

                    artist_instance, artist_created = Artist.get_or_create(
                        uri=artist["uri"],
                        name=artist["name"],
                        popularity=artist["popularity"]
                    )

                    if artist_created:
                        for genre in artist["genres"]:
                            genre_instance, _ = Genre.get_or_create(name=genre)

                            artist_instance.genres.add(genre_instance)

                    album_instance.artists.add(artist_instance)

            # Retrieve and save track features
            track_features = sp.audio_features(track["uri"])[0]
            track_instance, track_created = Track.get_or_create(
                uri=track["uri"],
                name=track["name"],
                duration_ms=track["duration_ms"],
                acousticness=track_features["acousticness"],
                danceability=track_features["danceability"],
                energy=track_features["energy"],
                instrumentalness=track_features["instrumentalness"],
                liveness=track_features["liveness"],
                loudness=track_features["loudness"],
                mode=track_features["mode"],
                speechiness=track_features["speechiness"],
                tempo=track_features["tempo"],
                time_signature=track_features["time_signature"],
                valence=track_features["valence"]
            )

            # Save album track
            AlbumTrack.get_or_create(
                album=album_instance.id,
                track=track_instance.id,
            )

            artists_data = track["artists"]
            track_artists_ids = []

            # Save track artists
            if track_created:
                for artist_data in artists_data:
                    artist = sp.artist(artist_data["uri"])

                    artist_instance, _ = Artist.get_or_create(
                        uri=artist["uri"],
                        name=artist["name"],
                        popularity=artist["popularity"]
                    )

                    track_instance.artists.add(artist_instance)
