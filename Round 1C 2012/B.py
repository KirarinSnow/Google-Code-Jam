#!/usr/bin/env python
#
# Problem: Out of Gas
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Uses http://mpmath.googlecode.com for arbitrary precision

from mpmath import *

# precision
mp.dps = 15

for case in range(int(raw_input())):
    print "Case #%d:" % (case+1)
    l = raw_input().split()
    d = mpf(l.pop(0))
    n, a = map(int, l)

    tt, xx = zip(*[map(mpf, raw_input().split()) for i in range(n)])

    # add final point (t, d) where t is the time that the other car gets there
    t = []
    x = []
    for i in range(n):
        if xx[i] <= d:
            t.append(tt[i])
            x.append(xx[i])
    if len(x) > 0 and x[-1] < d:
        j = len(x)
        v = (xx[j]-xx[j-1])/(tt[j]-tt[j-1])
        b = xx[j]-v*tt[j]
        tc = (d-b)/v
        x.append(d)
        t.append(tc)
        
    nn = len(x)

    accs = map(mpf, raw_input().split())
    
    for acc in accs:
        delay = mpf(0)
        for i in range(1, nn):
            if x[i] < mpf('0.5')*acc*(t[i]-delay)**mpf(2):
                delay += t[i]-(sqrt(mpf(2)*x[i]/acc)+delay)
        print sqrt(d*mpf(2)/acc)+delay
