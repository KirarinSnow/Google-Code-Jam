#!/bin/sh
#
# Problem: Old Magician
# Language: sh
# Author: KirarinSnow
# Usage: sh -f thisfile.sh <input.in >output.out


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
