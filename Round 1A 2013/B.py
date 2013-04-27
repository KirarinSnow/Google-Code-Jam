#!/usr/bin/env python
#
# Problem: Manage your Energy
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: For small only.


for case in range(int(raw_input())):
    e, r, n = map(int, raw_input().split())
    v = map(int, raw_input().split())
    
    q = [(e, 0, 0)]
    d = {}
    m = 0
    while q:
        u = q.pop(0)
        if u not in d:
            ce, cn, cg = u
            d[u] = True
            m = max(m, cg)
            if cn < n:
                for j in range(ce+1):
                    g = j*v[cn]
                
                    q.append((min(e, ce-j+r), cn+1, cg+g))

    ans = m
    print "Case #%d: %s" % (case+1, ans)
