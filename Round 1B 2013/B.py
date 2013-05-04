#!/usr/bin/env python
#
# Problem: Falling Diamonds
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Works only for small input.


from fractions import *

r = 0
l = 0
t = []
while r < 20: # only for small
    # iterate over diamond-shaped probability tables
    l += 2

    # top
    p = [Fraction(1)]
    r += 1
    s = [0]*l
    t.append((l, s, p))

    # expansion
    s = [1]+[0]*(l-1)
    for j in range(l):
        pp = []
        for i in range(len(p)+1):
            if i == 0 or i == len(p):
                pp.append(p[0]/2)
            else:
                pp.append(p[i]/2+p[i-1]/2)
        p = pp
        r += 1
        t.append((l, s, p))
        s = ([s[0]+1]+s)[:l]

    # contraction
    ps = range(l)
    for j in range(l-1):
        pp = []
        for i in range(len(p)-1):
            if i == 0 or i == len(p)-2:
                pp.append(p[0]+p[1]/2)
            else:
                pp.append(p[i]/2+p[i+1]/2)
        p = pp
        r += 1
        s = map(lambda x: len(p)-x, ps)
        t.append((l, s, p))
        ps = ([0]+ps)[:l]

    # bottom
    p = [Fraction(1)]
    r += 1
    s = map(lambda x: len(p)-x, ps)
    t.append((l, s, p))


for case in range(int(raw_input())):
    n, x, y = map(int, raw_input().split())
    l, s, p = t[n-1]
    
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
