import json
import spotipy

from dotenv import load_dotenv
from peewee import *
from rich import print
from spotipy.oauth2 import SpotifyOAuth

# Setup database

db = SqliteDatabase("database.db")


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
    name = CharField()


class Album(BaseModel):
    uri = CharField(unique=True)
    name = CharField()
    album_type = AlbumType()
    release_date = DateField()
    total_tracks = IntegerField()


class Lyrics(BaseModel):
    text = CharField()


class Track(BaseModel):
    uri = CharField(unique=True)
    duration_ms = IntegerField()
    lyrics = ForeignKeyField(Lyrics)
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


class TrackNumber(BaseModel):
    album = ForeignKeyField(Album)
    track = ForeignKeyField(Track)
    number = IntegerField()

    class Meta:
        primary_key = CompositeKey("album", "track")


class Artist(BaseModel):
    uri = CharField(unique=True)
    name = CharField()
    genres = ManyToManyField(Genre)
    popularity = IntegerField()


db.connect()
db.create_tables([Album, Artist, Genre, Lyrics, Track, TrackNumber])

# Load environment variables
load_dotenv()

# Create Spotify connection
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/redirect",
))

f = open("../dataset/data/mpd.slice.0-999.json")

playlists = json.load(f)["playlists"]

track = playlists[0]["tracks"][0]
track_uri = track["track_uri"].split(":")[2]

track_data = sp.track(track_uri)
album = track_data["album"]

Album.create(
    uri=album["uri"],
    name=album["name"],
    album_type=album["album_type"],
    release_date=album["release_date"],
    total_tracks=album["total_tracks"]
)
