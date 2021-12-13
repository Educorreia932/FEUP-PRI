#!/bin/sh

precreate-core music



# Start Solr in background mode so we can use the API to upload the schema
echo "\n--- solr start"
solr start
#echo "\n--- sleep 5"
sleep 5
cp /data/synonyms.txt /var/solr/data/music/synonyms.txt
echo "\n--- send schema"
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/music/schema
#echo "\n--- sleep 1"
sleep 3
echo "\n--- send db"
# Populate collection
bin/post -c music /data/database.json
#echo "\n--- sleep 1"
sleep 3
echo "\n--- solr restart"
# Restart in foreground mode so we can access the interface
solr restart -f
