#!/usr/bin/env python
#
# Problem: The Bored Traveling Salesman
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Works only on small.


from itertools import *

for case in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    c = [(raw_input(), i+1) for i in range(n)]
    f = [map(int, raw_input().split()) for i in range(m)]
    e = {}
    for x, y in f:
        if x not in e:
            e[x] = []
        if y not in e:
            e[y] = []
        e[x].append(y)
        e[y].append(x)

    m = ':'
    cs = sorted(c)
    s = cs[0][1]
    o = filter(lambda x: x != s, range(1, n+1))
    for p in permutations(o):
        d = [s]
        t = c[s-1][0]
        for v in p:
            while len(d) > 0 and v not in e[d[-1]]:
                d.pop()
            if len(d) == 0:
                break

            d.append(v)
            t += c[v-1][0]
        
        if len(t) == 5*n:
            m = min(m, t)

    ans = m
    print "Case #%d: %s" % (case+1, ans)
