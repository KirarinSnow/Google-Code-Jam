#!/usr/bin/python
#
# Problem: World Cup 2010
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Works only on small set.


from math import *

def compute():
    p = input()

    m = map(int, raw_input().split())
    rows = []
    for i in range(p):
        rows.append(map(int, raw_input().split()))
    
    
    s = [0]*((1<<p)-1)
    for x in range((1<<p) - 1):
        level = int(log(x+1, 2))
        pos = x-((1<<level) - 1)
        cover = range(((1<<p)>>level)*pos, ((1<<p)>>level)*(pos+1))

        mark = False
        for c in cover:
            inc = 0
            node = (1<<p)-1+c
            while node > 0:
                node = (node-1) / 2
                inc += s[node]
 
            if (p-inc)>m[c]:
                mark = True
                break
        if mark:
            s[x] = 1
    
    return sum(s)
    
for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
