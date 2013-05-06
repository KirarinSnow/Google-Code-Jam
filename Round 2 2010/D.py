#!/usr/bin/python
#
# Problem: Grazing Google Goats
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Uses http://mpmath.googlecode.com for arbitrary precision.
#           Apparently only works for the small input.


from operator import *
from mpmath import *

# precision
mp.dps = 40

def concave(c, p1, p2, p3):
    c12 = (atan2(p2[0]-p1[0], p2[1]-p1[1])-atan2(c[0]-p1[0], c[1]-p1[1]))%(2*pi)
    c13 = (atan2(p3[0]-p1[0], p3[1]-p1[1])-atan2(c[0]-p1[0], c[1]-p1[1]))%(2*pi)
    return c12 > c13

def intersect(c, x, y):
    a = map(sub, c, x)
    b = map(sub, y, x)
    f = reduce(add, map(mul, a, b))*1.0/reduce(add, map(mul, b, b))
    pa = map(lambda z: z*f, b)
    mp = map(add, x, pa)
    v = map(sub, mp, c)
    d = map(lambda j, k: j+2*k, c, v)
    return d

def triarea(x, y, z):
    return abs((x[0]*(y[1]-z[1]) + y[0]*(z[1]-x[1]) + z[0]*(x[1]-y[1]))/2.0)

def norm(v):
    return sqrt(sum(map(mul, v, v)))

def area(x, y, z, w):
    tri = triarea(x, y, z)
    a = map(sub, y, w)
    b = map(sub, z, w)

    angle = acos(reduce(add, map(mul, a, b))*1.0/norm(a)/norm(b))
    r = norm(a)
    sector = pi*r*r*angle/(2*pi)
    ta = atan2(*a)
    tb = atan2(*b)
    seg = sector - triarea(y, z, w)
    if (ta-tb)%(2*pi) > pi:
        seg = pi*r*r-seg
    return tri+seg
    
for case in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    
    ps = [map(int, raw_input().split()) for i in range(n)]
    qs = [map(int, raw_input().split()) for i in range(m)]
    
    a = []
    for q in qs:
            
        pp = map(lambda x: (atan2(x[0]-q[0], x[1]-q[1]), x), ps)
        pp.sort()

        for i in range(n):
            if (pp[(i+1)%n][0]-pp[i][0])%(2*pi) >= pi:
                pp = pp[i+1:] + pp[:i+1]
                break
        else:
            a.append(0.0)
            continue

        s = []
        for i, j in pp:
            while len(s) > 1 and concave(q, j, s[-1], s[-2]):
                s.pop()
            s.append(j)

        c = q
        ar = 0.0
        for i in range(len(s)):
            b = c
            if i == len(s)-1:
                c = q
            else:
                c = intersect(q, s[i], s[i+1])
            ar += area(q, b, c, s[i])

        a.append(ar)
        
    print "Case #%d: %s" % (case+1, ' '.join(map(lambda x: '%0.7f' % x, a)))
