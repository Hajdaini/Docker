#!/bin/bash

# Delete all stopped containers
docker rm $(docker ps -a -q)
# Remove all unused images
docker image prune -a
