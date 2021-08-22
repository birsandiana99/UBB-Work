#!/bin/bash

while `true`; do
    processes=`ps | awk '{ print $1" "$4 }' | grep -v '\(CMD\)\|\(5.sh\)'`
	
    for dang_proc in $@; do
        if [[ $processes == *$dang_proc* ]]; then
            pid=`ps | grep $dang_proc | awk '{ print $1 }'`
            kill $pid
        fi
    done
    sleep 2
done
