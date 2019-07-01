#!/bin/bash

# Delete all stopped containers
docker rm -f $(docker ps -a -q)
# Remove all unused images
docker image prune -a
