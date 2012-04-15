#!/bin/sed -f
#
# Problem: Speaking in Tongues
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed <input.in >output.out


1 s/.*/0<>0123456789/
1 h
1 d

y/ynficwlbkuomxsevzpdrjgthaq/abcdefghijklmnopqrstuvwxyz/

x
:inc
s/9</<0/
t inc
s/^</0</
s/\(.\)<\(.*\)>\(.*\1\(.\)\)/\4\2<>\3/
x
G
s/\(.*\)\n\(.*\)<.*/Case #\2: \1/
