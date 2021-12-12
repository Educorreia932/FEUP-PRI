import json
import os

from datetime import datetime, date
from models import *
from rich import print
from playhouse.shortcuts import model_to_dict
from tqdm import tqdm

def json_serial(obj):
    """JSON serializer for objects not serializable by default JSON code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

    raise TypeError (f"Type {obj} not serializable")

# Setup database
db.init(os.path.dirname(__file__) + "/data/database.db")

TrackArtist = Track.artists.get_through_model()
TrackAlbum = Track.albums.get_through_model()
AlbumArtist = Album.artists.get_through_model()
ArtistGenre = Artist.genres.get_through_model()

MAX_TRACKS = 250

tracks = list(Track.select().dicts().execute()[:MAX_TRACKS])

# Iterate over tracks
for track in tqdm(tracks):

    artists = []
    albums = []
    # Iterate over track artists
    track_artists = TrackArtist.select().where(TrackArtist.track_id == track["id"]).dicts().execute()

    for track_artist in track_artists:
        artist = model_to_dict(Artist.get(track_artist["artist"]))
        artist.pop("id")

        track_artist_genres = list(ArtistGenre.select().where(ArtistGenre.artist_id == track_artist["id"]).dicts().execute())

        genres = []

        # Iterate over artist genres
        for track_artist_genre in track_artist_genres:
            genres.append(model_to_dict(Genre.get(track_artist_genre["genre"]))["name"])

        artist["genres"] = genres

        artists.append(artist)

    track["artists"] = artists

    # Iterate over track albums
    track_albums = list(TrackAlbum.select().where(TrackAlbum.track_id == track["id"]).dicts().execute())

    for track_album in track_albums:
        album = model_to_dict(Album.get(track_album["album"]))
        album.pop("id")

        album_artists = list(AlbumArtist.select().where(AlbumArtist.album_id == track_album["id"]).dicts().execute())

        artists = []

        # Iterate over album artists
        for album_artist in album_artists:
            artist = model_to_dict(Artist.get(album_artist["artist"]))
            artist.pop("id")

            artists.append(artist)

        album["artists"] = artists

        albums.append(album)

    track["albums"] = albums

    track.pop("id")

# Save file
with open(os.path.dirname(__file__) + "/data/database.json", "w") as json_file:
    json.dump(tracks, json_file, default=json_serial)