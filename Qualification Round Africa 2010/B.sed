#!/bin/sed
#
# Problem: Reverse Words
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed <input.in >output.out

 
1 {s/.*/0<>0123456789/; h; d}


s/$/\n/
:reverse
s/^\([^\n ]*\) \(.*\n\)/\2 \1/
t reverse
s/\n//


x
:caseinc
s/9</<0/
t caseinc
s/^</0</
s/\(.\?\)<\(.*\)\(>.*\1\(.\)\)/\4\2<\3/
x
G
s/\(.*\)\n\(.*\)<.*/Case #\2: \1/
