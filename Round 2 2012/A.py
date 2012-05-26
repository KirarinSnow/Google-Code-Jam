#!/usr/bin/python
#
# Problem: Swinging Wild
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Times out on large input.


for i in range(int(raw_input())):
    n = int(raw_input())
    d, l = zip(*[map(int, raw_input().split()) for j in range(n)])
    D = int(raw_input())

    d = list(d) + [D]
    l = list(l) + [0]

    f = False
    s = set()
    q = [(0, 0)]
    
    while q:
        p, v = q.pop(0)
        if v == n:
            f = True
            break
        if (p, v) in s:
            continue

        s.add((p, v))

        t = min(l[v], d[v]-p)
        r = []
        w = v+1
        while w <= n and d[w]-d[v] <= t:
            r.append(w)
            w += 1
        for x in r:
            q.append((d[v], x))

    ans = "YES" if f else "NO"

    print "Case #%d: %s" % (i+1, ans)
