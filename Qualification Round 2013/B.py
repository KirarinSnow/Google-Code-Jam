#!/usr/bin/env python
#
# Problem: Lawnmower
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    l = [map(int, raw_input().split()) for i in range(n)]
    t = zip(*l)

    ans = "YES"
    for i in range(n):
        for j in range(m):
            if l[i][j] != max(l[i]) and l[i][j] != max(t[j]):
                ans = "NO"
                
    print "Case #%d: %s" % (case+1, ans)
