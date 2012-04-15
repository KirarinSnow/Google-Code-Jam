#!/usr/bin/env python
#
# Problem: Recycled Numbers
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    a, b = map(int, raw_input().split())
    l = len(str(a))

    c = 0
    for x in range(a, b+1):
        y = x
        for s in range(1, l):
            y = y%10**(l-1)*10 + y/10**(l-1)
            if x < y <= b:
                c += 1
            if y == x:
                break

    print "Case #%d: %d" % (case+1, c)
