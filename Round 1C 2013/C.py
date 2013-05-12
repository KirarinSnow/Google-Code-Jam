#!/usr/bin/env python
#
# Problem: The Great Wall
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Small only.


def process(q):
    for w, e, s in q:
        for i in range(w+Z, e+Z):
            c[i] = max(c[i], s)

for case in range(int(raw_input())):
    n = int(raw_input())
    f = [map(int, raw_input().split()) for i in range(n)]
    
    a = []
    for d, n, w, e, s, dd, dp, ds in f:
        for k in range(n):
            a.append((d, w, e, s))
            d += dd
            w += dp
            e += dp
            s += ds
    a.sort()

    Z = 250
    c = [0]*500
    v = 0
    
    cd = None
    for d, w, e, s in a:
        if d != cd:
            if cd != None:
                process(q)
            cd = d
            q = []
        if min(c[w+Z:e+Z]) < s:
            v += 1
            q.append((w, e, s))

    process(q)
           
    print "Case #%d: %d" % (case+1, v)
