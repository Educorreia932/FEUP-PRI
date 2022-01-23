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

genre = list(Genre.select().dicts().execute())

genreList = {"bruh"}

# Iterate over tracks
for genr in tqdm(genre):
    genreList.add(genr["name"])

genreL = list()

a = 0
for i in genreList:
    if(len(i.split()) > 1):
        genreL.append(i)
        a += 1
        if a >= 50:
            break

# Save file
with open(os.path.dirname(__file__) + "/data/genreListProtected.txt", "w") as json_file:
    for i in genreList:
        if len(i.split()) == 1:
            json_file.write(str(i) + "\n")
    for i in genreL:
        json_file.write(str(i) + "\n")

# Save file
with open(os.path.dirname(__file__) + "/data/genreListSynonyms.txt", "w") as json_file:
    for i in genreList:
        if len(i.split()) == 1:
            json_file.write(str(i) + " => " + str(i) + "|0.15\n")
    for i in genreL:
        json_file.write(str(i) + " => " + str(i) + "|0.15\n")

# Save file
with open(os.path.dirname(__file__) + "/data/multiWordGenreList.txt", "w") as json_file:
    json_file.write("(")
    for i in genreL:
        json_file.write("(" + str(i) + ")" + "|")
    json_file.write("[a-zA-Z0-9_]+)")