#!/usr/bin/env python
#
# Problem: New Lottery Game
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


L = 30

def f(n):
    x = bin(n+(1<<L))[3:]
    t = []
    for j in range(len(x)):
        if x[j] == '1':
            t.append(x[:j]+'0'+'.'*(len(x)-1-j))
    return t
            
def total(x, y, z):
    p = 1
    for i in range(L):
        c = min(x[i], y[i])+max(x[i], y[i])+z[i]
        b = {'000' : 1,
             '001' : 0,
             '00.' : 1,
             '010' : 1,
             '011' : 0,
             '01.' : 1,
             '110' : 0,
             '111' : 1,
             '11.' : 1,
             '.00' : 2,
             '.01' : 0,
             '.0.' : 2,
             '.10' : 1,
             '.11' : 1,
             '.1.' : 2,
             '..0' : 3,
             '..1' : 1,
             '...' : 4}
        p *= b[c]
    return p
        
for case in range(int(raw_input())):
    a, b, k = map(int, raw_input().split())
    s = 0
    for x in f(a):
        for y in f(b):
            for z in f(k):
                s += total(x, y, z)
                   
    print "Case #%d: %s" % (case+1, s)
