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
    artists = ManyToManyField(Artist)
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
db.create_tables([Album, AlbumTrack, Artist, Genre, Track])

# Load environment variables
load_dotenv()

# Create Spotify connection
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/redirect",
))

f = open("../dataset/data/mpd.slice.0-999.json")

playlists = json.load(f)["playlists"]
tracks = playlists[0]["tracks"]

for track_data in tracks:
    track_uri = track_data["track_uri"].split(":")[2]

    track = sp.track(track_uri)
    album = track["album"]
    artists_data = track["artists"]

    for artist_data in artists_data:
        artist = sp.artist(artist_data["uri"])

        Artist.replace(
            uri=artist["uri"],
            name=artist["name"],
            popularity=artist["popularity"]
        ).execute()

    Track.replace(
        uri=track["uri"],
        name=track["name"],
        duration_ms=track["duration_ms"],
        popularity=track["popularity"],
        lyrics="Lorem Ipsum",
        acousticness=-1,
        danceability=-1,
        energy=-1,
        instrumentalness=-1,
        liveness=-1,
        loudness=-1,
        mode=-1,
        speechiness=-1,
        tempo=-1,
        time_signature=-1,
        valence=-1
    ).execute()

    Album.replace(
        uri=album["uri"],
        name=album["name"],
        album_type=album["album_type"],
        release_date=album["release_date"],
        total_tracks=album["total_tracks"]
    ).execute()
