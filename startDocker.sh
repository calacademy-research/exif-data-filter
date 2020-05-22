#!/bin/bash
exif_container="exifContainer"

input_path=$1
output_path=$2
collection_id=$3

rel_path="`dirname \"$0\"`"
abs_path="`( cd \"$rel_path\" && pwd )`"

if [ ! "$(docker ps -q -f name=$exif_container)" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=$exif_container)" ]; then
        # cleanup
        docker rm $exif_container
    fi
    docker create -it -v $abs_path:/scripts \
    			     -v $input_path:/photos \
    			     -v $output_path:/output \
               --name $exif_container\
    			exif_image
fi
echo "Starting container with name: "
docker start $exif_container
echo "Executing filter..."
docker exec -it $exif_container /scripts/execPython.sh $collection_id
echo "Stopping container with following name: "
docker stop $exif_container
echo
echo "Filter complete! Find csv in "$output_path
