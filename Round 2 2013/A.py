#!/usr/bin/env python
#
# Problem: Ticket Swapping
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    s = [map(int, raw_input().split()) for i in range(m)]

    z = 0

    do = {}
    de = {}

    o, e, p = map(list, zip(*s))
    for i in range(m):
        if o[i] not in do:
            do[o[i]] = 0
        do[o[i]] += p[i]
        if e[i] not in de:
            de[e[i]] = 0
        de[e[i]] += p[i]

        k = e[i]-o[i]
        z += p[i]*(k*n-k*(k-1)/2)        

    o = sorted(list(set(o)))
    e = sorted(list(set(e)))
    q = []
    c = 0
    while len(o) > 0 or len(e) > 0:
        if len(o) == 0 or e[0] < o[0]:
            t = e.pop(0)
            x = de[t]
            while x > 0:
                v = min(q[-1][1], x)
                x -= v
                q[-1][1] -= v
                r = q[-1][0]
                k = t-r
                h = v*(k*n-k*(k-1)/2)
                c += h
                if q[-1][1] == 0:
                    q.pop()
        else:
            t = o.pop(0)
            q.append([t, do[t]])
        
    ans = (z-c)%1000002013
    print "Case #%d: %s" % (case+1, ans)
