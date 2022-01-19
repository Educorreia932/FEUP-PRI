#!/bin/sh

precreate-core music

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 2

cp /data/synonyms.txt /var/solr/data/music/synonyms.txt
cp /data/enumsConfig.xml /var/solr/data/music/enumsConfig.xml
cp /data/genreList.txt /var/solr/data/music/genreList.txt
cp /data/genreList.txt /var/solr/data/music/genreListSynonyms.txt
cp /data/genreList.txt /var/solr/data/music/genreListProtected.txt

# Send schema
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/music/schema

sleep 2

# Populate collection
bin/post -c music /data/database.json

sleep 1

# Restart in foreground mode so we can access the interface
solr restart -f
