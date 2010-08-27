#!/usr/bin/env python
#
# Problem: Millionaire
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: May be too slow for large.


from math import *

MAX = 1000000

def compute():
    m, p, x = raw_input().split()
    m = int(m)
    p = float(p)
    x = int(x)

    if x >= MAX:
        return 1.0

    if x < 1.0/(1<<m):
        return 0.0

    d = [[0.0] * ((1<<m)+1) for i in range(m+1)]
    d[0][1] = 1.0
    for j in range(1, m+1):
        d[j][1] = p**j
        d[j][1<<j] = 1.0
        for i in range(2, (1<<j)):
            c = 0.0
            for k in range((i+1)/2, (1<<(j-1))+1):
                if i-k >= 0:
                    c = max(c, p*d[j-1][k] + (1-p)*d[j-1][i-k])
            d[j][i] = c

    return d[m][int((1<<m)*((x+0.0)/MAX))]
    

for i in range(input()):
    print "Case #%d: %0.6f" % (i+1, compute())
