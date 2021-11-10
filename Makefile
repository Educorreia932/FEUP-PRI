target := database.db

all: data/database.db

data/database.db: populate lyrics
	
populate:
	@echo "Populating database..."
	@python3 src/populate.py

lyrics: 
	@echo "Retrieving lyrics..."
	@python3 src/lyrics.py

clean:
	@rm -rf data/database.db

# out/charts/*:


