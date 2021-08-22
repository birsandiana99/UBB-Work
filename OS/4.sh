#!/bin/bash

for filename in `find $1`; do
    if [ -L $filename ]; then
        if ! [ -e $filename ]; then
            echo $filename "- The file that this file is pointing does not exist anymore :("
        fi
    fi
done
