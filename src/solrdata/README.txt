# No path com a Dockerfile
docker build . -t <nome_do_projeto>
docker run -p 8983:8983 <nome_do_projeto>

# Para ver o nome do container: docker container ls
# Music é o nome do container, definido no startup.sh
docker exec <nome_do_container> bin/post -c music ../../data/database.json