#!/bin/bash

input_path=$1
output_path=$2
collection_id=$3

echo
echo "DAM ExifTool Filter Starting..."
echo "Got input path: "$input_path
echo "Got output path: "$output_path
echo "Got collection id: "$collection_id
echo
echo "Now creating docker container with the following name and id: "

rel_path="`dirname \"$0\"`"
abs_path="`( cd \"$rel_path\" && pwd )`"
outer_dir="`dirname \"$abs_path\"`"
docker_source=$outer_dir"/docker_files"
echo $docker_source
cd $docker_source
./startDocker.sh $input_path $output_path $collection_id
