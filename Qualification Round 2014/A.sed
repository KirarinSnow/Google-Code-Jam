#!/bin/sed -f
#
# Problem: Magic Trick
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed <input.in >output.out


1 s/.*/0<>0123456789/
1 h
1 d


s/^/>/
: read
/>/! N
s/\n/>/
s/#//
N
N
N
N
/>1/ s/>.\n\([^\n]*\)\n.*/#\1/
/>2/ s/>.\n[^\n]*\n\([^\n]*\)\n.*/#\1/
/>3/ s/>.\n[^\n]*\n[^\n]*\n\([^\n]*\)\n.*/#\1/
/>4/ s/>.\n[^\n]*\n[^\n]*\n[^\n]*\n\([^\n]*\)/#\1/
/^#/ b read

s/#/ # /
s/^/ /
s/$/ /

: repeat
s/^\(.*\) \([0-9]\+\) \(.*\) \2 /%\2 \1 \3 /
t repeat

/%/! s/.*/Volunteer cheated!/
/%.*%/ s/.*/Bad magician!/
/^%/ s/^%\([0-9]\+\).*/\1/


x
: increment
s/9</<0/
t increment
s/^</0</
s/\(.\?\)<\(.*\)\(>.*\1\(.\)\)/\4\2<\3/
x

G
s/\(.*\)\n\(.*\)<.*/Case #\2: \1/
