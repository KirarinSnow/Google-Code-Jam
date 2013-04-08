#!/usr/bin/python
#
# Problem: Number Game
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from math import *

for case in range(int(raw_input())):
    a1, a2, b1, b2 = map(int, raw_input().split())

    phi = (1+sqrt(5))/2
    p1, p2 = 1/phi, phi

    c = 0
    for i in range(a1, a2+1):
        c += max(0, 1+min(b2, int(floor(i*p2)))-max(b1, int(ceil(i*p1))))
    ans = (1+a2-a1)*(1+b2-b1)-c

    print "Case #%d: %s" % (case+1, ans)
