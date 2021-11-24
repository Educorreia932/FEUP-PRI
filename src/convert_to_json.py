import os

from models import *
from rich import print
from playhouse.shortcuts import model_to_dict
from tqdm import tqdm

# Setup database
db.init(os.path.dirname(__file__) + "/../data/database.db")

TrackArtist = Track.artists.get_through_model()

tracks = Track.select().dicts().execute()

# Iterate over tracks
for track in tqdm(tracks):
    # Iterate over track artists
    artists = []

    track_artists = TrackArtist.select().where(TrackArtist.track_id == track["id"]).dicts().execute()

    for track_artist in track_artists:
        artist = model_to_dict(Artist.get(track_artist["id"]))

        artists.append(artist)

    track["artists"] = artists
