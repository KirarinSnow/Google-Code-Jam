#!/usr/bin/env python
#
# Problem: Building a House
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    c, r = map(int, raw_input().split())
    b = [raw_input() for i in range(r)]
    for j in range(len(b)):
        b[j] = map(lambda x: x=='G' or x=='S', b[j])
    
    h = [[0]*(c+1) for i in range(r)]
    for i in range(c):
        for j in range(r):
            if not b[j][i]:
                h[j][i] = 0
            elif j == 0:
                h[j][i] = 1
            else:
                h[j][i] = 1+h[j-1][i]
    
    m = 0
    for x in range(r):
        s = [(0, -1)]
        for y in range(c+1):
            l = (h[x][y], y)
            while s and h[x][y] <= s[-1][0]:
                l = s.pop()
                m = max(m, (y-l[1])*l[0])
            s.append((h[x][y], l[1]))
            
    return m        

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
