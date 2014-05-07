#!/usr/bin/env python
#
# Problem: City Tour
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n = int(raw_input())
    p = [map(int, raw_input().split()) for i in range(n-3)]

    w = [[0]*n for i in range(n)]
    for i in range(3):
        for j in range(i+1, 3):
            w[i][j] = 1
    for i in range(n-3):
        x, y = p[i]
        w[x-1][i+3] = 1
        w[y-1][i+3] = 1
    
    b = 0
    for i in range(2, n)[::-1]:
        q = []
        for j in range(i):
            if w[j][i] > 0:
                q.append(j)
        x, y = q
        b = max(b, w[x][y]+w[x][i]+w[y][i])
        w[x][y] = max(w[x][y], w[x][i]+w[y][i])

    print "Case #%d: %s" % (case+1, b)
