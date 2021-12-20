# Information Retrieval

## Instructions

To build and run the Docker image:

```shell
docker build -t solr:latest . 
docker run --rm -p 8983:8983 -t -i solr:latest
```

To check a container's ID:

```shell
docker ps
```

To execute a command:

```shell
docker exec <container_id> <command>
```
