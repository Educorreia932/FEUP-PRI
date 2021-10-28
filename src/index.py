import json
import spotipy

from rich import print
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID="511e04ae8586475cbf6b4b0914228bee"
SPOTIPY_CLIENT_SECRET="4d9bcb0f2ad548928b345c05a08f286b"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri="http://127.0.0.1:8000/redirect",
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))

f = open("../dataset/data/mpd.slice.0-999.json")

playlists = json.load(f)["playlists"]

track = playlists[0]["tracks"][0]

print(sp.track(track["track_uri"].split(":")[2]))
