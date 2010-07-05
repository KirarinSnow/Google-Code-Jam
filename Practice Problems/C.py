#!/usr/bin/python
#
# Problem: Egg Drop
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Fails on large set.


t = []
s = 100
bs = 100

for i in range(s+1):
    t.append([])
    for j in range(bs+1):
        t[i].append(0)

for b in range(bs+1):
    for d in range(b,s+1):
        if b == 0:
            t[d][b] = 0
        else:
            if d ==b:
                t[d][b] = 2**d - 1
            else:
                t[d][b] = 1 + t[d-1][b-1] + t[d-1][b]

def compf(d,b):
    return t[d][b]

def compd(f,b):
    d = 1    
    while 1:
        bb = 1
        while bb <= b:
            if t[d][bb] >= f:
                return d
            bb +=1 
        d+=1

def compb(f,d):
    b = 0
    while t[d][b] < f:
        b+=1
    return b

for i in range(input()):
    q, d, b = map(int, raw_input().split())
    
    ff = t[d][b]
    if ff > 2**32:
        ff = -1
    
    print "Case #%d: %d %d %d" % (i+1, ff, compd(q,b), compb(q,d))
