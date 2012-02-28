#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 문제: 약속장소 정하기
# 언어: Python
# 저자: KirarinSnow
# 사용: python thisfile.py <input.in >output.out


import heapq

MAX = 1<<30

for case in range(1, input()+1):
    n, p, m = map(int, raw_input().split())
    f = [map(int, raw_input().split()) for i in range(p)]
    r = [map(int, raw_input().split()) for i in range(m)]

    w, l, c = zip(*map(lambda x: (x[0], x[1], x[2:]), r))

    x, v = zip(*f)

    e = [{} for j in range(n)]

    for i in range(m):
        for j in range(l[i]-1):
            a = c[i][j]-1
            b = c[i][j+1]-1
            if b not in e[a]:
                e[a][b] = MAX
            if a not in e[b]:
                e[b][a] = MAX
            e[a][b] = min(e[a][b], w[i])
            e[b][a] = min(e[b][a], w[i])
    
    d = [[MAX for i in range(n)] for i in range(p)]
    
    for i in range(p):
        xx = x[i]-1
        vv = v[i]

        d[i][xx] = 0
        s = [False]*n
        
        q = []
        for j in range(n):
            heapq.heappush(q, [d[i][j], j])
        while q:
            ds, z = heapq.heappop(q)
            if not s[z]:
                s[z] = True
                nb = e[z].keys()
                for y in nb:
                    d[i][y] = min(d[i][y], d[i][z] + vv*e[z][y])
                    heapq.heappush(q, [d[i][y], y])

    u = MAX
    for i in range(n):
        u = min(u, max(map(lambda z: d[z][i], range(p))))
            
    ans = u if u < MAX else -1
    print "Case #%d: %d" % (case, ans)
