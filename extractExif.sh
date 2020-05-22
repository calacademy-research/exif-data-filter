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

./startDocker.sh $input_path $output_path $collection_id
