#!/usr/bin/env python
#
# Problem: Hot Dog Proliferation
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Small only.


for case in range(int(raw_input())):
    g = [0]*(10**7*2+10**5*2+1)
    c = int(raw_input())
    x = [map(int, raw_input().split()) for i in range(c)]
    s = []
    for p, v in x:
        g[p] = v
        s.append(p)
    s.sort(key=lambda x: g[x])
    
    t = 0
    while s:
        p = s.pop()
        if g[p] > 1:
            m = g[p]/2
            t += m
            g[p] %= 2
            g[p+1] += m
            g[p-1] += m
            s.append(p+1)
            s.append(p-1)
    
    ans = t

    print "Case #%d: %s" % (case+1, ans)
