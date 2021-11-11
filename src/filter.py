import sqlite3
import pandas as pd
import os

import sqlalchemy as sqla
import sqlalchemy_utils as sqla_utils
from rich import print
from better_profanity import profanity


def has_swear_word(text):
    if text == None:
        return False
    words = text.split()
    for w in words:
        for sw in swear_words:
            if sw.lower() == w.lower():
                return True
    return False


#Connect to database
con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "../data/database.db"))

album = pd.read_sql_query("SELECT * from album", con)
album_artist_through = pd.read_sql_query("SELECT * from album_artist_through", con)
albumtrack = pd.read_sql_query("SELECT * from albumtrack", con)
artist = pd.read_sql_query("SELECT * from artist", con)
artist_genre_through = pd.read_sql_query("SELECT * from artist_genre_through", con)
genre = pd.read_sql_query("SELECT * from genre", con)
track = pd.read_sql_query("SELECT * from track", con)
track_artist_through = pd.read_sql_query("SELECT * from track_artist_through", con)
#close the connection
con.close()

#Check null values
print("Check if there are null values")
print("Album")
print(album.isnull().any(axis=1).any())
print("AlbumArtist")
print(album_artist_through.isnull().any(axis=1).any())
print("AlbumTrack")
print(albumtrack.isnull().any(axis=1).any())
print("Artist")
print(artist.isnull().any(axis=1).any())
print("ArtistGenre")
print(artist_genre_through.isnull().any(axis=1).any())
print("Genre")
print(genre.isnull().any(axis=1).any())
print("Track")
print(track.isnull().any(axis=1).any())

print("TrackArtist")
print(track_artist_through.isnull().any(axis=1).any())

#Flag innappropriate content

#Get swear word list
with open(os.path.join(os.path.dirname(__file__), "../src/swear_word_list.txt"), 'r') as f:
    swear_words = [line.strip() for line in f]


#Artist
artist['explicit'] = artist['name'].apply(lambda x: has_swear_word(x))
#print("Number of censored artist names:")
#print(artist['explicit'].value_counts(normalize=False))

#Track
track['explicitname'] = track['name'].apply(lambda x: has_swear_word(x))
#print("Number of censored track names:")
#print(track['explicitname'].value_counts(normalize=False))

track['explicittrack'] = track['lyrics'].apply(lambda x: has_swear_word(x))
#print("Number of censored track lyrics:")
#print(track['explicittrack'].value_counts(normalize=False))

track['explicit'] = track['explicitname'] | track['explicittrack']
#print("Number of censored track lyrics or names:")
#print(track['explicit'].value_counts(normalize=False))

track.drop(columns=['explicittrack', 'explicitname'], inplace=True)


#Album
album['explicit'] = album['name'].apply(lambda x: has_swear_word(x))
#print("Number of censored album names:")
#print(album['explicit'].value_counts(normalize=False))

#Save into new database
engine = sqla.create_engine("sqlite:///" +  os.path.join(os.path.dirname(__file__), "../data/database_filtered.db"))

if not sqla_utils.database_exists(engine.url):
    sqla_utils.create_database(engine.url)


with engine.begin() as connection:
    album.to_sql('album', engine, if_exists="replace", index=False)
    album_artist_through.to_sql('album_artist_through', engine, if_exists="replace", index=False)
    albumtrack.to_sql('albumtrack', engine, if_exists="replace", index=False)
    artist.to_sql('artist', engine, if_exists="replace", index=False)
    artist_genre_through.to_sql('artist_genre_through', engine, if_exists="replace", index=False)
    genre.to_sql('genre', engine, if_exists="replace", index=False)
    track.to_sql('track', engine, if_exists="replace", index=False)
    track_artist_through.to_sql('track_artist_through', engine, if_exists="replace", index=False)
    engine.execute("PRAGMA foreign_keys = ON")
    engine.execute("DELETE FROM track WHERE name == \"\" OR name IS NULL;")
    engine.execute("DELETE FROM track WHERE lower(name) LIKE '%instrumental%';")
    engine.execute("DELETE FROM album WHERE name == \"\" OR name IS NULL;")
    engine.execute("DELETE FROM album WHERE lower(name) LIKE '%instrumental%';")
    engine.execute("DELETE FROM artist WHERE lower(name) LIKE '%instrumental%';")
    engine.execute("DELETE FROM artist WHERE name == \"\" OR name IS NULL;")
    engine.execute("DELETE FROM genre WHERE name == \"\" OR name IS NULL;")
    


engine.dispose()