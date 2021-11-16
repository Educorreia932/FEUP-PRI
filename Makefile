target := database.db

all: data/database.db

data/database.db: populate lyrics filter
	
# Iterate over playlists present in the JSON dataset file
# For each playlist, retrieve its tracks' information from Spotify API
# Do the same for the track's artists and albums
# Save retrieved information in the database
populate:
	@echo "Populating database..."
	@python3 src/populate.py

# Iterate over tracks and their respective artists, that are already stored in the database
# Retrieve the lyrics for each track by scraping its Genius webpage entry
# Save lyrics to the database
lyrics: 
	@echo "Retrieving lyrics..."
	@python3 src/lyrics.py

# Filter incorrect information from database
filter:
	@jupyter nbconvert --to python out/stats.ipynb
	@echo "Filtering database..."
	@python3 notebooks/filter.py

# Generate charts that allow to better analyze the dataset
out/charts/*:
	@jupyter nbconvert --to python notebooks/stats.ipynb
	@echo "Generating charts..."
	@python3 notebooks/stats.py

clean:
	@rm -rf data/database.db
