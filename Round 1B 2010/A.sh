#!/bin/sh
#
# Problem: File Fix-it
# Language: bash
# Author: KirarinSnow
# Usage: bash thisfile.sh <input.in >output.out



compute()
{
    rm -r /tmp/tmp
    mkdir /tmp/tmp

    read n m
    for i in `seq 1 $n`
    do
	read p
	mkdir -p /tmp/tmp$p
    done
    for i in `seq 1 $m`
    do
	read p
	mkdir -vp /tmp/tmp$p
    done | wc -l
}


read case
for i in `seq 1 $case`
do
    echo -n Case \#$i:\ 
    compute
done
