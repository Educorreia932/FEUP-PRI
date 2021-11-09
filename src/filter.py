import os
import sqlite3

from rich import print

db = sqlite3.connect(os.path.join(os.path.dirname(__file__), "../dataset/database.db"))

db_cursor = db.cursor()

#Get null or empty name tracks
db_cursor.execute("SELECT * FROM Track WHERE name IS NULL OR name == \"\"")
print(db_cursor.fetchall())

#Get null or empty name tracks
db_cursor.execute("SELECT * FROM Album WHERE name IS NULL OR name == \"\"")
print(db_cursor.fetchall())

#db_cursor.execute("SELECT * FROM Track Left JOIN (Album Left JOIN albumtrack ON (Album.id == albumtrack.album_id))")
#print(db_cursor.fetchone())