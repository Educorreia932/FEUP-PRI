FROM solr:8.10

COPY data/database.json /data/database.json

COPY data/schema_without_filters.json /data/schema_without_filters.json
COPY data/schema_with_filters.json /data/schema_with_filters.json

COPY data/synonyms.txt /data/synonyms.txt

COPY startup.sh /scripts/startup.sh

ENTRYPOINT [ "/scripts/startup.sh" ]