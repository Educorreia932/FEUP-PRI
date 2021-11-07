import json
import os
import spotipy

from dotenv import load_dotenv
from models import *
from peewee import *
from rich import print
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm

# Setup database

database_path = os.path.join(os.path.dirname(__file__), "../out/database/database.db")

db.init(database_path)
db.create_tables([Album, AlbumTrack, Artist, Genre, Track, Track.artists.get_through_model()])

# Load environment variables
load_dotenv()

# Create Spotify connection
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/redirect",
))

f = open(os.path.join(os.path.dirname(__file__), "../dataset/data/mpd.slice.0-999.json"))

playlists = json.load(f)["playlists"]

for playlist in tqdm(playlists):
    playlist_track_uris = []

    for playlist_track in playlist["tracks"]:
        playlist_track_uris.append(playlist_track["track_uri"].split(":")[2])

    for i in range(0, len(playlist_track_uris), 50):
        track_uris = playlist_track_uris[i:i + 50]
        tracks = sp.tracks(track_uris)["tracks"]

        for track in tracks:
            album = track["album"]

            # Save album
            album_id = Album.replace(
                uri=album["uri"],
                name=album["name"],
                album_type=album["album_type"],
                release_date=album["release_date"],
                total_tracks=album["total_tracks"]
            ).execute()

            # Get album tracks. Only reads 50 at a time
            album_tracks_info = sp.album_tracks(album["uri"])

            # Start getting album tracks from this offset
            offset = 0

            # Used to simulate a do while loop
            still_reading_tracks = True

            while album_tracks_info["next"] != None or still_reading_tracks:
                offset += 50

                if album_tracks_info["next"] == None:
                    still_reading_tracks = False

                album_track_num = 0

                # Read from every track in the album
                for album_track in album_tracks_info["items"]:
                    album_track_num = album_track_num + 1

                    lyrics = "Lorem Ipsum"

                    if "popularity" not in album_track:
                        album_track["popularity"] = -1

                    track_features = sp.audio_features(album_track["uri"])[0]
                    track_id = Track.replace(
                        uri=album_track["uri"],
                        name=album_track["name"],
                        duration_ms=album_track["duration_ms"],
                        popularity=album_track["popularity"],
                        lyrics=lyrics,
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
                    ).execute()

                    AlbumTrack.replace(
                        album=album_id,
                        track=track_id,
                        track_number=album_track_num
                    ).execute()
                    artists_data = album_track["artists"]
                    track_artists_ids = []

                    track_instance = Track.get(track_id)

                    # Save track artists
                    for artist_data in artists_data:
                        artist = sp.artist(artist_data["uri"])

                        artist_id = Artist.replace(
                            uri=artist["uri"],
                            name=artist["name"],
                            popularity=artist["popularity"]
                        ).execute()

                        track_instance.artists.add(Artist.get(artist_id))

                # Get next n tracks
                if still_reading_tracks:
                    album_tracks_info = sp.album_tracks(album["uri"])
