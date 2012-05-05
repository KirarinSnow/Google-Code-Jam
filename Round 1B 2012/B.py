#!/usr/bin/python
#
# Problem: Tide Goes In, Tide Goes Out
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from heapq import *

MAX = 1<<30

def compute():
    h, n, m = map(int, raw_input().split())
    c = [map(int, raw_input().split()) for i in range(n)]
    f = [map(int, raw_input().split()) for i in range(n)]

    d = {}
    q = []
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                heappush(q, [0, (0, i, j)])

    while q:
        t, u = heappop(q)

        if u in d:
            continue
        d[u] = t
        vs = []

        wl = max(0, h-10*t)

        st, x, y = u
        if x == n-1 and y == m-1:
            return t

        cc = c[x][y]
        cf = f[x][y]
        cw = max(cf, wl)
        
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if 0 <= i < n and 0 <= j < m:
                nc = c[i][j]
                nf = f[i][j]
                
                nst = st
                cp = 1
                if cf <= nc-50 and nf <= nc-50 and nf <= cc-50:
                    if wl <= nc-50:
                        tr = 0
                        nwl = wl
                    else:
                        tr = (wl-(nc-50))/10.0
                        nwl = nc-50
                        cp = 0

                    if nwl >= cf+20:
                        tt = 1+tr
                    else:
                        tt = 10+tr

                    if st == 0 and cp == 1:
                        nt = 0
                    elif st == 0 and cp == 0:
                        nst = 1
                        nt = tt
                    else:
                        nt = t + tt

                    vs.append([nt, (nst, i, j)])
                        
        for v in vs:
            heappush(q, v)

for i in range(input()):
    print "Case #%d: %0.7f" % (i+1, compute())
