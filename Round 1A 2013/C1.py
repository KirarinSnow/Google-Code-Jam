#!/usr/bin/env python
#
# Problem: Good Luck
# Language: Python
# Author: KirarinSnow
# Usage: pypy thisfile.py <input.in >output.out


from itertools import *
from math import *

for case in range(int(raw_input())):
    r, n, m, k = map(int, raw_input().split())
    
    q = [i for i in combinations_with_replacement(range(2, m+1), n)]
    s = len(q)

    d = []
    p = []
    z = {}
    g = factorial(n)
    for c, comb in enumerate(q):
        v = list(set(comb))
        w = g
        for i in v:
            w /= factorial(comb.count(i))

        d.append(w)

        p.append(dict())
        
        pset = chain.from_iterable(combinations(comb, r) for r in range(n+1))

        for sub in pset:
            prod = reduce(lambda x, y: x*y, sub, 1)
            if prod not in p[c]:
                p[c][prod] = 0
            p[c][prod] += 1
            if prod not in z:
                z[prod] = 0
            z[prod] += w

    nq = len(q)

    print "Case #%d:" % (case+1)

    for trial in range(r):
        prs = map(int, raw_input().split())
        
        maxp = 0.0
        best = None

        for c in range(nq):
            pr = d[c]
                
            for prod in prs:
                if pr < maxp:
                    pr = 0.0
                    break
                if prod not in p[c]:
                    pr = 0.0
                    break
                pr *= 1.0 * p[c][prod] / z[prod]

            if pr > maxp:
                maxp = pr
                best = q[c]
        print ''.join(map(str, best))
