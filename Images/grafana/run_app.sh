#!/bin/bash

docker build -t grafana .
docker-compose up -d # remove the -d to see errors from the docker-compose
