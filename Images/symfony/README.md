# symfony

## Description

Symfony docker image with phpmyadmin and mysql

## How to ?

**`Please first change in the file docker-compose.yml the word [YOUR APP FULL PATH] by the full symfony project path from your local machine`**

- Run the image and container :

```shell
chmod 770 run_app.sh
./run_app.sh
```
Then visit the http://[YOUR CONTAINER_IP]:3569

- Go in the tty of the container :

```shell
docker exec -ti sf_app_c /bin/bash
```

- Restart server :

```shell
docker rm -f sf_app_c && docker-compose up -d
```

### Debug
 
- debug only the last 100 lines of the log file :

```shell
docker logs --tail=100 --timestamps sf_app_c
```

- debug the log file permanently :

```shell
docker logs -f --tail --timestamps sf_app_c
```
