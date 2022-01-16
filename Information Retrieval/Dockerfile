FROM solr:8.10

COPY data/database.json /data/database.json
COPY data/synonyms.txt /data/synonyms.txt
COPY data/schema.json /data/schema.json
COPY data/enumsConfig.xml /data/enumsConfig.xml
COPY data/genreList.txt /data/genreList.txt
COPY data/genreList.txt /data/genreListSynonyms.txt
COPY data/genreList.txt /data/genreListProtected.txt
COPY config/web.xml /opt/solr-8.10.1/server/solr-webapp/webapp/WEB-INF/web.xml

COPY startup.sh /scripts/startup.sh

ENTRYPOINT [ "/scripts/startup.sh" ]