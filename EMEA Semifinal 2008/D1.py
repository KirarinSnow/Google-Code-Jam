#!/usr/bin/env python
#
# Problem: Bus Stops
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from itertools import *

def mult(m, n):
    o = [[0]*len(n[0]) for j in range(len(m))]
    for i in range(len(o)):
        for j in range(len(o[0])):
            c = 0
            for k in range(len(m[0])):
                c += m[i][k] * n[k][j]
                c %= 30031
            o[i][j] = c
    return o

def exp(m, x):
    z = [m]
    v = []
    while x:
        z.append(mult(z[-1], z[-1]))
        v.append(x%2)
        x >>= 1
    
    c = [[0]*len(m) for j in range(len(m))]
    for k in range(len(c)):
        c[k][k] = 1

    for i in range(len(v)):
        if v[i] == 1:
            c = mult(c, z[i])
    return c

def compute():
    n, k, p = map(int, raw_input().split())
    c = list(combinations(range(p-1), k-1))
    d = len(c)

    s = [[0] for j in range(d-1)] + [[1]]
    m = [[0]*d for j in range(d)]
    for j in range(d):
        pre = c[j]
        for jj in range(d):
            post = c[jj]
            for b in pre:
                if tuple(map(lambda x: x-1,
                             filter(lambda x: x!=b, pre)) + [p-2]) == post:
                    m[j][jj] = 1
                if tuple(map(lambda x: x-1, pre)) == post:
                    m[j][jj] = 1

    s = mult(exp(m, n-k), s)
    return s[-1][0]

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
