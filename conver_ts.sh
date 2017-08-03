#!/bin/bash

for FN in $@
do
    OUT=`echo $FN | sed "s/.ts/.mkv/"`
    echo $FN
    echo $OUT

    ffmpeg-3.3.2-64bit-static/ffmpeg -i $FN  -c:v copy -c:a aac $OUT
done


