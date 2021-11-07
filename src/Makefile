target := database.db

all: dependencies $(all_python_files)

dependencies:
	sudo apt install python3-pip
	pip3 spoinstall json os dotenv peewee rich spotipy tqdm geniuspy

database.db:
	python index.py