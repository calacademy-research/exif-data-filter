#!/bin/bash
rel_path="`dirname \"$0\"`"
abs_path="`( cd \"$rel_path\" && pwd )`"
outer_dir="`dirname \"$abs_path\"`"
cd $outer_dir
docker build -t exif_image docker_files
