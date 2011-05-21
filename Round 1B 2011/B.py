#!/usr/bin/python
#
# Problem: Revenge of the Hot Dogs
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Fails on large.


def compute():
    p = []
    c, d = map(int, raw_input().split())
    for i in range(c):
        pl, v = map(int, raw_input().split())
        p.extend([pl]*v)
    b = True
    for j in range(1, len(p)):
        if p[j]-p[j-1] < d:
            b = False
    if b:
        return 0.0
    else:
        q = []
        for j in range(1, len(p)):
            q.append(p[j]-p[j-1])
        u = 1e12
        l = 0
        while u-l > 1e-9:
            t = (u+l)/2
            v = -1
            for y in q:
                v = v - (y-d)/t
                if v < -1:
                    v = -1
                if v > 1:
                    l = t
                    break
            else:
                u = t
                           
        return u


for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
