#!/usr/bin/env pypy
#
# Problem: Data Packing
# Language: Python
# Author: KirarinSnow
# Usage: pypy thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n, x = map(int, raw_input().split())
    s = map(int, raw_input().split())
    s.sort()
    p = []
    c = []
    for k in s[::-1]:
        j = 0
        while j < len(p):
            if p[j]+k <= x and c[j] < 2:
                p[j] += k
                c[j] += 1
                break
            j += 1
        if j == len(p):
            p.append(k)
            c.append(1)

    ans = len(p)
                
    print "Case #%d: %s" % (case+1, ans)
