#!/bin/bash
#
# Problem: Alien Language
# Language: bash
# Author: KirarinSnow
# Usage: bash -f thisfile.sh <input.in >output.out


read length words cases

wd=1
ws=''
while [ $wd -le $words ]
do
    read word
    ws="$ws $word"
    wd=$(($wd + 1))
done

num=1
while [ $num -le $cases ]
do
    echo -n Case \#$num:\ 
    read line
    echo $ws | tr ' ' '\n' | grep `echo $line | tr '()' '[]'` | wc -l
    num=$(($num + 1))
done
