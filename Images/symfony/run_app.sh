#!/bin/bash

docker build -t sf_app .
docker-compose up -d # remove the -d to see errors from docker-compose
