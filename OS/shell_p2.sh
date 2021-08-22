#!/bin/bash

count=0
for filename in `find -name "*.c"`
do
  if [ -f $filename ]; then
      nr_lines=`cat $filename|wc -l`
      if [ $nr_lines -gt 500 ]; then
          echo $filename
	  count=`expr $count + 1`
      fi
      if [ $count -eq 10 ]; then
	  break
      fi
  fi
done

