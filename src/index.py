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


class Album(BaseModel):
    name = CharField()
    uri = CharField()
    album_type = AlbumType()


class Lyrics(BaseModel):
    text = CharField()


class Track(BaseModel):
    duration_ms = IntegerField()
    lyrics = ForeignKeyField(Lyrics)


class TrackPosition(Model):
    album = ForeignKeyField(Album)
    track = ForeignKeyField(Track)

    class Meta:
        primary_key = CompositeKey('album', 'track')


class Artist(BaseModel):
    name = CharField()


class Genre(BaseModel):
    name = CharField()


db.connect()
db.create_tables([Album, Track, Lyrics, Artist, Genre])

# Load environment variables
load_dotenv() 

# Create Spotify connection
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/redirect",
))

f = open("../dataset/data/mpd.slice.0-999.json")

playlists = json.load(f)["playlists"]

track = playlists[0]["tracks"][0]

print(sp.track(track["track_uri"].split(":")[2]))
