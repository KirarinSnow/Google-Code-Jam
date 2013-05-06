#!/usr/bin/python
#
# Problem: Grazing Google Goats
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Exports to PARI/GP for precision computing.


from operator import *
from math import *
from fractions import *
from os import *

def concave(c, p1, p2, p3):
    c12 = (atan2(p2[0]-p1[0], p2[1]-p1[1])-atan2(c[0]-p1[0], c[1]-p1[1]))%(2*pi)
    c13 = (atan2(p3[0]-p1[0], p3[1]-p1[1])-atan2(c[0]-p1[0], c[1]-p1[1]))%(2*pi)
    return c12 > c13

def intersect(c, x, y):
    a = map(sub, c, x)
    b = map(sub, y, x)

    f = reduce(add, map(mul, a, b))/reduce(add, map(mul, b, b))
    pa = map(lambda z: z*f, b)
    mp = map(add, x, pa)
    v = map(sub, mp, c)
    d = map(lambda j, k: j+2*k, c, v)
    return d

def triarea(x, y, z):
    return abs((x[0]*(y[1]-z[1]) + y[0]*(z[1]-x[1]) + z[0]*(x[1]-y[1]))/2)

def snorm(v):
    return sum(map(mul, v, v))

def area(x, y, z, w):
    tri = triarea(x, y, z)
    a = map(sub, y, w)
    b = map(sub, z, w)
    c = map(sub, y, z)

    rs = snorm(a)

    rat = 1-snorm(c)/snorm(a)/2
    sector = "%d/%d*acos(%d/%d)" % \
        (rs.numerator, rs.denominator*2, rat.numerator, rat.denominator)

    ta = atan2(*map(lambda x: 1.0*x, a))
    tb = atan2(*map(lambda x: 1.0*x, b))

    stri = -triarea(y, z, w)
    
    if (ta-tb)%(2*pi) > pi:
        stri *= -1
        sector = "%d/%d*Pi-%s" % (rs.numerator, rs.denominator, sector)
    return tri+stri, sector
    

for case in range(int(raw_input())):
    system('echo -n "Case #%d: "' % (case+1))
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
            system('echo -n "0.0 "')
            continue
        
        s = []
        for i, j in pp:
            while len(s) > 1 and concave(q, j, s[-1], s[-2]):
                s.pop()
            s.append(j)

        q = map(Fraction, q)
        s = map(lambda x: map(Fraction, x), s)

        c = q
        tri = Fraction(0)
        sect = []
        for i in range(len(s)):
            b = c
            if i == len(s)-1:
                c = q
            else:
                c = intersect(q, s[i], s[i+1])
            ar = area(q, b, c, s[i])
            tri += ar[0]
            sect.append(ar[1])
        
        gp = '+'.join(['%d/%d' % (tri.numerator, tri.denominator)] + sect)
        system('echo "print1(%s)" | gp -f -q | tr " E\n" "0e "' % gp)

    system('echo')
