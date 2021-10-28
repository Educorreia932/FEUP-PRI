import json
import spotipy

from dotenv import load_dotenv
from rich import print
from spotipy.oauth2 import SpotifyOAuth

load_dotenv() 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/redirect",
))

f = open("../dataset/data/mpd.slice.0-999.json")

playlists = json.load(f)["playlists"]

track = playlists[0]["tracks"][0]

print(sp.track(track["track_uri"].split(":")[2]))
