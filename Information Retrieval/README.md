## How to run

```
docker build . -t elastic-search
docker run -p 8983:8983 elastic-search
```

# Para ver o nome do container: docker container ls
# Music é o nome do container, definido no startup.sh
docker exec <nome_do_container> bin/post -c music ../../data/database.json