import os
import re

from dotenv import load_dotenv
from lyricsgenius import Genius
from models import *
from peewee import *
from tqdm import tqdm

# Load environment variables
load_dotenv()

# Setup Genius
genius = Genius(remove_section_headers=True, verbose=False)

# Setup database
db.init(os.path.dirname(__file__) + "/../data/database.db")

TrackArtist = Track.artists.get_through_model()

tracks = Track.select()

for track in tqdm(tracks):
    artist = track.artists[0]

    try:
        lyrics = genius.search_song(track.name, artist.name).lyrics

    except Exception:
        continue

    Track.update(lyrics=lyrics).where(Track.id == track.id).execute()
    
