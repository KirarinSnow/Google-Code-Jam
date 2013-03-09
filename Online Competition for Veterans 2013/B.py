#!/usr/bin/env python
#
# Problem: Baby Height
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from math import *

def height(x):
    f, i = map(int, x[:-1].split("'"))
    return f*12+i

for case in range(int(raw_input())):
    l = raw_input().split()
    g = l[0]
    m, f = map(height, l[1:])

    h = (m+f+(-5, 5)[g == 'B'])/2.0

    ans = ' to '.join(map(lambda x: "%d'%d\"" % (x/12, x%12),
                          (ceil(h-4), floor(h+4))))
    print "Case #%d: %s" % (case+1, ans)
