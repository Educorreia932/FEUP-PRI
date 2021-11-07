from peewee import *

db = SqliteDatabase(None)

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
