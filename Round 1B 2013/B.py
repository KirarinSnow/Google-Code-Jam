#!/usr/bin/env python
#
# Problem: Falling Diamonds
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


import sys
sys.setrecursionlimit(2000)

from fractions import *
from math import *

def row(n):
    if n in d:
        return d[n]

    o = int(floor(sqrt(9+8*(n-1))-3)/4.0)+1
    l = o*2
    r = 4*o+1
    q = 2*o*(o-1)+o-1
    i = n-q-1
    
    if i <= r/2: # top half
        p = [Fraction(1)/(1<<i)]
        for j in range(i):
            p.append(p[-1]*(i-j)/(j+1))
        s = map(lambda x: max(0, i-x), range(i))
        
        d[n] = l, s, p
    else: # bottom half
        l, ps, pp = row(n-1)
        pp = map(float, pp)
        p = []
        for k in range(len(pp)-1):
            p.append((pp[k]+pp[k+1])/2)
        p[0] += pp[0]/2
        p[-1] += pp[-1]/2
        s = [r-i]*(l-r+i)+range(1, r-i+1)[::-1]
        d[n] = l, s, p
    return d[n]

d = {}

for case in range(int(raw_input())):
    n, x, y = map(int, raw_input().split())

    l, s, p = row(n)
    
    x = abs(x)
    if y < -x + l-1: # inside heap
        ans = 1.0
    elif y > -x + l+1: # outside heap
        ans = 0.0
    else: # edge of heap
        try:
            ans = float(sum(p[:s[y]]))
        except:
            ans = 0.0
    
    print "Case #%d: %s" % (case+1, ans)
