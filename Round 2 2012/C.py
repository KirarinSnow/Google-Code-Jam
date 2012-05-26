#!/usr/bin/python
#
# Problem: Mountain View
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


import sys

sys.setrecursionlimit(3000)

def trav(x):
    for j in e[x]:
        trav(j)
    t.append(x)

def assign(x, h, slope):
    a[x] = h
    for y in e[x]:
        p = int(h-slope*(x-y))-1
        slope2 = (h-p)*1.0/(x-y)
        assign(y, p, slope2)
        slope = slope2
        
for i in range(int(raw_input())):
    n = int(raw_input())
    x = map(lambda y: int(y)-1, raw_input().split())

    e = [[] for j in range(n)]
    
    for j in range(n-1):
        e[x[j]].append(j)

    t = []
    trav(n-1)
    if sorted(t) != t:
        ans = "Impossible"
    else:
        a = [None]*n
        assign(n-1, 0, 0.0)
        m = min(a)
        ans = ' '.join(map(lambda z: str(z-m), a))
    
    print "Case #%d: %s" % (i+1, ans)
