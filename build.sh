#!/bin/bash

IMAGE_NAME=xtract-matio

docker rmi -f $IMAGE_NAME

docker build -t $IMAGE_NAME .
