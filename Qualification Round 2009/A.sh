#!/bin/sh
#
# Problem: Alien Language
# Language: sh
# Author: KirarinSnow
# Usage: sh -f thisfile.sh <input.in >output.out

read length words cases

wd=1
ws=''
while [ $wd -le $words ]
do
    read word
    ws=$ws\\n$word
    wd=$(($wd + 1))
done

num=1
while [ $num -le $cases ]
do
    echo -n Case \#$num:\ 
    read line
    echo $ws | grep `echo $line | tr '()' '[]'` | wc -l
    num=$(($num + 1))
done
