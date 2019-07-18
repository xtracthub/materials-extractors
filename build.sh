#!/bin/bash

IMAGE_NAME=materials_extractors_image

docker rmi -f $IMAGE_NAME

docker build -t $IMAGE_NAME .
