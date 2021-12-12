## How to run

```shell
docker build -t elastic-search . 
docker run -p 8983:8983 -t -i elastic-search
```

To check a container's ID.

```shell
docker ps
```

To execute a command.

```shell
docker exec <container_id> <command>
```

