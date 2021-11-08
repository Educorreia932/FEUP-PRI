target := database.db

all: data/database.db

data/database.db:
	@echo "Populating database..."
	@python3 src/populate.py

clean:
	@rm -rf data/*

# out/charts/*:

# TODO: Clean data and process
