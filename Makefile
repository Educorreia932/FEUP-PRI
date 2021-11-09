target := database.db

all: data/database.db

data/database.db:
	@echo "Populating database..."
	@python3 src/populate.py
# TODO: Clean data and process

clean:
	@rm -rf data/database.db

# out/charts/*:


