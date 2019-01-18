#!/bin/bash

docker build -t logger .
docker-compose up -d # remove the -d to see errors from docker-compose
