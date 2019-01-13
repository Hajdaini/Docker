#!/bin/bash


if [ $# -eq 1 ]
    then pid=$(docker inspect --format '{{ .State.Pid }}' "$1")
    ls -al /proc/$pid/ns
else
     echo "usage : <./namespace.sh [CONTAINER ID|NAME]"
fi