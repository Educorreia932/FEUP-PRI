FROM solr:8.10

COPY data/database.json /data/database.json
COPY data/schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT [ "/scripts/startup.sh" ]