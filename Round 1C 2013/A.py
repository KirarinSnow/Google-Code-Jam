#!/usr/bin/env python
#
# Problem: Consonants
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


V = list('aeiou')

for case in range(int(raw_input())):
    s, n = raw_input().split()
    n = int(n)
    l = len(s)
    
    b = []
    c = 0
    for i in range(l):
        if s[i] not in V:
            c += 1
            if c >= n:
                b.append((i-n+1, i+1))
        else:
            c = 0

    q = 0
    for i in range(len(b)):
        if i == 0:
            p = 0
        else:
            p = b[i-1][0]+1
        x = b[i][0]-p+1
        y = l-b[i][1]+1
        q += x*y

    print "Case #%d: %d" % (case+1, q)
