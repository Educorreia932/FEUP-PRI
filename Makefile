target := database.db

all: dependencies $(all_python_files)

dependencies:
	sudo apt install python3-pip
	pip3 install -r requirements.txt

database.db:
	python3 src/index.py
	