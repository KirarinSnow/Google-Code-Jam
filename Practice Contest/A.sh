#!/bin/bash
#
# Problem: Old Magician
# Language: bash
# Author: KirarinSnow
# Usage: bash -f thisfile.sh <input.in >output.out


compute()
{
    read w b
    
    if [ $(($b % 2)) -eq 1 ]
    then
	echo BLACK
    else
	echo WHITE
    fi
}


read case
num=1
while [ $num -le $case ]
do
    echo -n Case \#$num:\ 
    compute
    num=$(($num + 1))
done
