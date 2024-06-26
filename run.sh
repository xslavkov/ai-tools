#!/bin/bash

# Check if an argument was provided
if [ $# -eq 0 ]; then
    echo "No arguments provided"
    exit 1
fi

docker run -it --rm --name python -v "$PWD":/app/src -w /app/src python python $1
