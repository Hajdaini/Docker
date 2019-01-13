# Description:
Docker image to configure your ansible environment

# Configuration :
Imagine you have 2 remote servers with this config :

- Serveur1 :
  - hostname: "webServer1"
  - ip: "192.168.1.50"

- Serveur2 :
  - hostname: "webServer2"
  - ip: "192.168.1.51"

You will need to those files:
### hosts
```yaml
[test]
webServer1 ansible_host=192.168.1.50
webServer2 ansible_host=192.168.1.51
```

### the lines bellow of Dockerfile
```Dockerfile
RUN sshpass -p <YOUR_ROOT_REMOTE_MACHINE_PASSWORD> ssh-copy-id -f -o StrictHostKeyChecking=no root@192.168.1.50
RUN sshpass -p <YOUR_ROOT_REMOTE_MACHINE_PASSWORD> ssh-copy-id -f -o StrictHostKeyChecking=no root@192.168.1.51
```
### the lines bellow of docker-compose.yml
```docker-compose
extra_hosts:
  - "server1:192.168.1.50"
  - "server2:192.168.1.51"
```

## Additional configuration

- The name of the image is ***ansible_image*** if you want to change it, then change the tag (option -t) of the build command and also change the option ***"image: [YOUR_NEW_IMAGE_NAME]"*** in the file ***docker-compose.yml*** with your new image name

- If you want to change the name of the container then change the option ***"container_name: [YOUR_NEW_CONTAINER_NAME]"*** in the file ***docker-compose.yml*** with your new container name and modify it also in the script run.sh (-ti option of the exec command)

# How to run it :
run the command bellow
```
root@docker:~# cd [YOUR_IMAGE_PATH]
root@docker:~# docker build -t ansible_image . 
root@docker:~# chmod 770 run.sh # do it once
root@docker:~# ./run.sh
```
