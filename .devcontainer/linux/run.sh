#!/bin/sh

xhost +local:root

docker run -it \
    --net=host \
    --ipc=host \
    -e DISPLAY=$DISPLAY \
    gatorrover:latest
    
