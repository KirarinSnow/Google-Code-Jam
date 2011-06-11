#!/usr/bin/python
#
# Problem: Irregular Cakes
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


from math import *

def compute():
    w, l, u, g = map(int, raw_input().split())
    ls = [map(int, raw_input().split()) for i in range(l)]
    us = [map(int, raw_input().split()) for i in range(u)]
    lt = []
    ut = []
    while len(ls) > 0 and len(us) > 0:
        if ls[0][0] == us[0][0]:
            lt.append(ls.pop(0))
            ut.append(us.pop(0))
        elif ls[0][0] < us[0][0]:
            m = (ut[-1][1]-us[0][1])*1.0/(ut[-1][0]-us[0][0])
            b = (us[0][0]*ut[-1][1]-us[0][1]*ut[-1][0])*1.0/(us[0][0]-ut[-1][0])
            f = m*ls[0][0]+b
            ut.append([ls[0][0], f])
            lt.append(ls.pop(0))
        else:
            m = (lt[-1][1]-ls[0][1])*1.0/(lt[-1][0]-ls[0][0])
            b = (ls[0][0]*lt[-1][1]-ls[0][1]*lt[-1][0])*1.0/(ls[0][0]-lt[-1][0])
            f = m*us[0][0]+b
            lt.append([us[0][0], f])
            ut.append(us.pop(0))
    a = []
    for i in range(len(lt)):
        a.append([lt[i][0], ut[i][1]-lt[i][1]])
    
    p = [0]
    for i in range(1, len(a)):
        p.append(p[-1]+(a[i][0]-a[i-1][0])*(a[i][1]+a[i-1][1])/2.0)
    t = p[-1]*1.0

    c = 0
    for i in range(1, g):
        while p[c] < t*i/g:
            c += 1
        q = t*i/g - p[c-1]
        m = (a[c-1][1]-a[c][1])*1.0/(a[c-1][0]-a[c][0])
        b = (a[c][0]*a[c-1][1]-a[c][1]*a[c-1][0])*1.0/(a[c][0]-a[c-1][0])
        b += a[c-1][1]
        v = a[c-1][0]
        A = m
        B = b-m*v
        C = -v*b-2*q
        if -1e-8 < A < 1e-8:
            x = (q/(p[c]-p[c-1]))*(a[c][0]-a[c-1][0])+a[c-1][0]
        else:
            x = ((-B)+sqrt(B*B - 4*A*C))/2/A
        print "%0.6f" % x
        
for i in range(input()):
    print "Case #%d:" % (i+1)
    compute()
