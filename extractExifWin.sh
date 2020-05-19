#!/bin/bash
script_path=$(readlink -f $0)
dir_path=$(dirname "$script_path")
the_python_file=/main.py
the_python_file_path=$dir_path$the_python_file

python3 the_python_file_path -i $1 -c $2 -o $3
