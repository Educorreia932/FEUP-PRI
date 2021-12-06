target := database.db

all: data/database.db

data/database.db: populate lyrics filter
	
# Populate database with Spotify data
populate:
	@echo "Populating database..."
	@python3 src/populate.py

# Update track lyrics
lyrics: 
	@echo "Retrieving lyrics..."
	@python3 src/lyrics.py

# Filter incorrect information from database. Also adds the explicit boolean to tracks, artists and albums and other miscellaneous filtering
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
