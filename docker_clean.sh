#!/bin/sh
echo "========================================================================"
echo "Delete the container"
docker ps -q -a | xargs docker rm
echo "========================================================================"
echo "delete all the images"
docker rmi $(docker images | grep "<none>" | awk '{print $3}')
echo "========================================================================"
echo "deleting all untagged images"
docker rmi $(docker images -q)
echo "========================================================================"
echo "Deleting all the dangling volume"
for v in $(sudo docker volume ls -qf 'dangling=true'); do sudo docker volume rm "$v"; done
echo "========================================================================"




