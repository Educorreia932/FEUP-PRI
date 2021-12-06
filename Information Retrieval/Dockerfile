FROM solr:8.10

COPY data/database.json /data/database.json
# COPY data/test_schema.json /data/test_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]