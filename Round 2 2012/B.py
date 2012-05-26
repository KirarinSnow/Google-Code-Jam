#!/usr/bin/python
#
# Problem: Aerobics
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


from random import *

def c(x1, y1, r1, x2, y2, r2):
    return (x2-x1)**2 + (y2-y1)**2 < (r1+r2)**2

for i in range(int(raw_input())):
    n, w, l = map(int, raw_input().split())
    r = map(int, raw_input().split())

    p = sorted(range(n), key = r.__getitem__)[::-1]
    r = sorted(r)[::-1]

    x = [(0.0, 0.0, r[0])]
    for j in range(1, n):
        s = False
        while not s:
            px = random()*w
            py = random()*l
            s = True
            for k in range(len(x)):
                if c(x[k][0], x[k][1], x[k][2], px, py, r[j]):
                    s = False
                    break
        x.append((px, py, r[j]))

    z = [None]*n

    for j in range(n):
        z[p[j]] = (x[j][0], x[j][1])
        
    ans = ' '.join(map(lambda y: ' '.join(map(str, y)), z))

    print "Case #%d: %s" % (i+1, ans)
