#!/bin/sed -f
#
# Problem: Odd Man Out
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed <input.in >output.out

 
1 {s/.*/0<>0123456789/; h; d}


/^[0-9]*$/d

s/ /  /g
s/^/ /
s/$/ /
:delete
s/ \([0-9]\+\) \(.*\) \1 /\2/
t delete
s/ //g


x
:caseinc
s/9</<0/
t caseinc
s/^</0</
s/\(.\?\)<\(.*\)\(>.*\1\(.\)\)/\4\2<\3/
x
G
s/\(.*\)\n\(.*\)<.*/Case #\2: \1/
