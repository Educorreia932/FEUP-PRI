import os

from models import *
from rich import print
from playhouse.shortcuts import model_to_dict
from tqdm import tqdm

# Setup database
db.init(os.path.dirname(__file__) + "/../data/database.db")

TrackArtist = Track.artists.get_through_model()
ArtistGenre = Artist.genres.get_through_model()

tracks = Track.select().dicts().execute()

# Iterate over tracks
for track in tqdm(tracks):
    # Iterate over track artists
    artists = []

    track_artists = TrackArtist.select().where(TrackArtist.track_id == track["id"]).dicts().execute()

    for track_artist in track_artists:
        artist = model_to_dict(Artist.get(track_artist["artist"]))

        track_artist_genres = ArtistGenre.select().where(ArtistGenre.artist_id == track_artist["id"]).dicts().execute()

        genres = []

        # Iterate over artist genres
        for track_artist_genre in track_artist_genres:
            genre = model_to_dict(Genre.get(track_artist_genre["genre"]))

            genres.append(genre["name"])

        artist["genres"] = genres

        artists.append(artist)

        print(artist)

    track["artists"] = artists

    break 

