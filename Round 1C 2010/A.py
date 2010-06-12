#!/usr/bin/python
#
# Problem: Rope Intranet
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    n = input()
    r = []
    
    for i in range(n):
        r.append(map(int,raw_input().split()))

    c = 0
    for i in range(n):
        for j in range(i):
            if (r[i][0] - r[j][0]) * (r[i][1] - r[j][1]) < 0:
                c+=1
    return c

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
