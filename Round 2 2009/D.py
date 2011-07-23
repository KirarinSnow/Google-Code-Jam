#!/usr/bin/python
#
# Problem: Watering Plants
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Times out on large.


from math import *

def compute():
    def out(v, w):
        return sqrt((v[0]-w[0])**2 + (v[1]-w[1])**2) > w[2] - v[2] + 1e-6

    n = input()
    p = [map(int, raw_input().split()) for i in range(n)]

    l = min(map(lambda x: x[2], p))+0.0
    u = 708.0

    while u-l > 1.0e-6:
        r = (l+u)/2
        c = []
        for c1 in range(n):
            for c2 in range(c1+1, n):
                x1, y1, r1 = p[c1]
                x2, y2, r2 = p[c2]
                
                x0 = sqrt((x1-x2)**2 + (y1-y2)**2)
                xp = ((r-r1)**2 - (r-r2)**2)/2.0/x0 + x0/2.0
                try:
                    yp = sqrt((r-r1)**2 - xp**2)
                    yn = -yp
                    cos = (x2-x1)/x0
                    sin = (y2-y1)/x0

                    x = cos*xp - sin*yp + x1
                    y = cos*yp + sin*xp + y1
                    v = cos*xp - sin*yn + x1
                    w = cos*yn + sin*xp + y1
                    
                    c.append((x, y, r))
                    c.append((v, w, r))
                except:
                    pass
        
        c.extend(map(lambda z: (z[0], z[1], r), p))

        for d in c:
            for e in c:
                for z in p:
                    if out(z, d) and out(z, e):
                        break
                else:
                    break
            else:
                continue
            break
        else:
            l = r
            continue
        u = r
    
    return r

for i in range(input()):
    print "Case #%d: %0.6f" % (i+1, compute())
