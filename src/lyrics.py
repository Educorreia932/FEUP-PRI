import os
import re

from dotenv import load_dotenv
from lyrics_extractor import SongLyrics, LyricScraperException
from models import *
from peewee import *
from tqdm import tqdm

# Load environment variables
load_dotenv()

# Setup database
db.init(os.path.dirname(__file__) + "/../data/database.db")

extract_lyrics = SongLyrics("AIzaSyDmZhnh3tsbCoYQmTdwMBP_WKNYg-kzzZ0", "dd09d107e1d0774a2")

TrackArtist = Track.artists.get_through_model()

tracks = Track.select(Track, TrackArtist, Artist).join(TrackArtist).join(Artist)

for track in tqdm(tracks):
    artist = track.artists[0]
        
    lyrics = extract_lyrics.get_lyrics(f"{track.name}-{artist.name}")["lyrics"]

    if lyrics:
         # Remove headers
        lyrics = re.sub(r"\[Intro\](.*\n)+?\n", "", lyrics)
        lyrics = re.sub(r"\[.*\]", "", lyrics)

        print(lyrics)

        Track.update(lyrics=lyrics).where(Track.id == track.id).execute()
