#!/bin/sh

precreate-core music

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Populate collection
bin/post -c music /data/database.json

# Restart in foreground mode so we can access the interface
solr restart -f
