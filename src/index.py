import json
import os
import spotipy

from dotenv import load_dotenv
from lyricsgenius import Genius
from peewee import *
from rich import print
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm

# TODO: Process the lyrics in a separate script

# Setup database

database_path = os.path.join(os.path.dirname(__file__), "database.db")
db = SqliteDatabase(database_path)


class BaseModel(Model):
    class Meta:
        database = db


class AlbumType(IntegerField):
    def __init__(self):
        choices = [
            (1, "album"),
            (2, "single"),
            (3, "compilation")
        ]

        self.to_db = {v: k for k, v in choices}
        self.from_db = {k: v for k, v in choices}
        super(IntegerField, self).__init__()


class Genre(BaseModel):
    name = CharField(unique=True)


class Artist(BaseModel):
    uri = CharField(unique=True)
    name = CharField()
    genres = ManyToManyField(Genre)
    popularity = IntegerField()


class Album(BaseModel):
    uri = CharField(unique=True)
    name = CharField()
    album_type = AlbumType()
    release_date = DateField()
    total_tracks = IntegerField()
    artists = ManyToManyField(Artist)


class Track(BaseModel):
    uri = CharField(unique=True)
    name = CharField()
    duration_ms = IntegerField()
    lyrics = CharField()
    artists = ManyToManyField(Artist, backref="tracks")
    popularity = IntegerField()
    acousticness = FloatField()
    danceability = FloatField()
    energy = FloatField()
    instrumentalness = FloatField()
    liveness = FloatField()
    loudness = FloatField()
    mode = IntegerField()
    speechiness = FloatField()
    tempo = FloatField()
    time_signature = IntegerField()
    valence = FloatField()


class AlbumTrack(BaseModel):
    album = ForeignKeyField(Album)
    track = ForeignKeyField(Track)
    track_number = IntegerField()

    class Meta:
        primary_key = CompositeKey("album", "track")


db.connect()
db.create_tables([Album, AlbumTrack, Artist, Genre, Track,
                 Track.artists.get_through_model()])

# Load environment variables
load_dotenv()

# Initialize Genius
genius = Genius()

# Create Spotify connection
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/redirect",
))

f = open("../dataset/data/mpd.slice.0-999.json")

playlists = json.load(f)["playlists"]

for playlist in playlists:
    for track_data in tqdm(playlist["tracks"]):
        track_uri = track_data["track_uri"].split(":")[2]

        track = sp.track(track_uri)
        album = track["album"]
        artists_data = track["artists"]
        track_artists_ids = []

        track_features = sp.audio_features(track_uri)[0]

        # song = genius.search_song(track["name"], artists_data[0]["name"])

        # if song is not None:
        #     lyrics = song.lyrics

        # else:
        #     lyrics = None

        lyrics = "Lorem Ipsum"

        # Save track
        track_id = Track.replace(
            uri=track["uri"],
            name=track["name"],
            duration_ms=track["duration_ms"],
            popularity=track["popularity"],
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

        # Save album
        Album.replace(
            uri=album["uri"],
            name=album["name"],
            album_type=album["album_type"],
            release_date=album["release_date"],
            total_tracks=album["total_tracks"]
        ).execute()
