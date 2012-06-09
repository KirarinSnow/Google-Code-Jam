#!/usr/bin/python
#
# Problem: Shoot the Target
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from math import *

MAX = 1<<25

def ang(c):
    a1 = atan2(y1, x1-c)%(2*pi)
    a2 = atan2(y2, x2-c)%(2*pi)
    return abs(a2-a1)/pi*180
    
def bs(l, u):
    while u-l > 1e-8:
        m1 = (u+l+l)/3.0
        m2 = (u+u+l)/3.0
        
        ang1 = ang(m1)
        ang2 = ang(m2)
        
        if ang2 > ang1:
            l = m1
        else:
            u = m2
    return l
    
for i in range(int(raw_input())):
    x1, y1, x2, y2 = map(int, raw_input().split())

    s = (y2-y1)*1.0/(x2-x1)
    if s == 0:
        xi = bs(-MAX, MAX)
        ans = ang(xi)
    else:
        b = y1-s*x1
        k = -b/s
        xi1 = bs(-MAX, k)
        xi2 = bs(k, MAX)
        ans = max(ang(xi1), ang(xi2))

    print "Case #%d: %s" % (i+1, ans)
