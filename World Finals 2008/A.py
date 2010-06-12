#!/usr/bin/python
#
# Problem: Juice
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Times out on large.


def compute():
    n = input()
    p = []
    for i in range(n):
        p.append(map(int, raw_input().split()))
    
    fs = set(map(lambda x: x[0], p))
    ss = set(map(lambda x: x[1], p))
    
    m = 0
    for f in fs:
        for s in ss:
            q = 10000 - f - s
            c = 0
            if q >= 0:
                for i in range(n):
                    if f >= p[i][0] and s >= p[i][1] and q >= p[i][2]:
                        c+=1
            m = max(m, c)

    return m

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
