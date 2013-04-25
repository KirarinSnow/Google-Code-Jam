#!/usr/bin/env python
#
# Problem: Bacteria
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 

     
for case in range(int(raw_input())):
    r = int(raw_input())
    s = [map(int, raw_input().split()) for i in range(r)]

    c = [[] for i in range(r)]
    d = list(range(r))

    for i in range(r):
        p = s[i]
        z = []
        for j in range(i):
            q = s[j]
            w = max(p[2], q[2])-min(p[0], q[0])+1
            h = max(p[3], q[3])-min(p[1], q[1])+1
            aw = p[2]-p[0]+q[2]-q[0]+2
            ah = p[3]-p[1]+q[3]-q[1]+2
            if w <= aw and h <= ah:
                if p[0] == q[2]+1 and p[1] == q[3]+1:
                    f = False
                elif q[0] == p[2]+1 and q[1] == p[3]+1:
                    f = False
                else:
                    f = True
            else:
                f = False
            
            if f:
                jj = j
                while d[jj] != jj:
                    jj = d[jj]
                d[jj] = i

    for j in range(r):
        jj = d[j]
        while d[jj] != jj:
            jj = d[jj]
        c[jj].append(j)

    m = 0
    for k in filter(lambda x: len(x) > 0, c):
        x2, y2 = map(lambda y: max(map(lambda x: s[x][y], k)), (2, 3))
        v = min(map(lambda x: s[x][0]+s[x][1], k))
        m = max(m, x2+y2-v+1)

    print "Case #%d: %d" % (case+1, m)
