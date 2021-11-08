SHELL := bash

all: %.html

%.html:
	@for url in $(shell cat example.txt); do \
		echo $${url} | sed 's|.*/||' | xargs touch; \
	done
