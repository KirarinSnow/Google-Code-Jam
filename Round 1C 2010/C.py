#!/usr/bin/python
#
# Problem: Making Chess Boards
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


from heapq import *

def process(r1, r2, c1, c2):
    for i in range(r1, r2):
        for j in range(c1, c2):
            if 0 <= i < m and 0 <= j < n:
                if g[i][j] == None:
                    s[i][j] = 0
                elif i == 0 or j == 0:
                    s[i][j] = 1
                elif g[i-1][j] != g[i][j] and g[i][j-1] != g[i][j] and \
                        g[i-1][j-1] == g[i][j]:
                    s[i][j] = 1 + min(s[i-1][j], s[i][j-1], s[i-1][j-1])
                else:
                    s[i][j] = 1
                heappush(q, (-s[i][j], i, j))

def clear(r1, r2, c1, c2):
    for i in range(r1, r2):
        for j in range(c1, c2):
            if 0 <= i < m and 0 <= j < n:
                g[i][j] = None
                
for case in range(int(raw_input())):
    m, n = map(int, raw_input().split())
    v = [eval('0x'+raw_input()) for i in range(m)]
    g = map(lambda x: map(lambda y: (x>>y)%2, range(n)[::-1]), v)
    
    s = [[1 for i in range(n)] for j in range(m)]
    q = []
                                              
    process(0, m, 0, n)

    b = []
    while q:
        x, r, c = heappop(q)
        if x != 0 and s[r][c] == -x:
            b.append((-x, r, c))
            clear(r+x+1, r+1, c+x+1, c+1)
            process(r+x+1, r-x+1, c+x+1, c-x+1)

    vs = sorted(list(set(map(lambda x: x[0], b))))[::-1]
    print "Case #%d: %d" % (case+1, len(vs))
    for k in vs:
        print k, len(filter(lambda x: x[0] == k, b))
