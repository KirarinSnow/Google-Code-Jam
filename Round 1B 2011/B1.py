#!/usr/bin/python
#
# Problem: Revenge of the Hot Dogs
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


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
        u = int(1e12)
        l = 0
        while u-l > 0:
            t = (u+l)/2
            v = -t
            for y in q:
                v = v - 2*(y-d)
                if v < -t:
                    v = -t
                if v > t:
                    l = t+1
                    break
            else:
                u = t
                           
        return u/2.0


for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
