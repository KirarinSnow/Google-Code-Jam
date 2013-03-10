#!/usr/bin/python
#
# Problem: Spinning Blade
# Language: Python
# Author: KirarinSnow
# Usage: pypy thisfile.py <input.in >output.out 
# Comments: Runs in 7 minutes using pypy for the large input.


mb = []
for i in range(500):
    mb.append([])
    for j in range(500):
        mb[i].append(None)
s = []
for i in range(500):
    s.append([])
    for j in range(500):
        s[i].append(None)

def compute():
    r, c, d = map(int, raw_input().split())
    g = [map(int, raw_input()) for i in range(r)]
    for i in range(r):
        for j in range(c):
            mi = g[i][j]+d
            mb[i][j] = (mi, i*mi, j*mi)

    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                s[i][j] = mb[i][j]
            elif i == 0:
                s[i][j] = map(lambda k: s[i][j-1][k] + mb[i][j][k], range(3))
            elif j == 0:
                s[i][j] = map(lambda k: s[i-1][j][k] + mb[i][j][k], range(3))
            else:
                s[i][j] = map(lambda k: s[i-1][j][k] + s[i][j-1][k] -
                              s[i-1][j-1][k] + mb[i][j][k], range(3))

    tm = -1
    for r1 in range(r):
        for c1 in range(c):
            for r2 in range(r1+2, r):
                if c1 + (r2-r1) < c:
                    c2 = c1 + (r2-r1)
                    
                    m = [0]*3
                    for k in range(3):
                        m[k] = s[r2][c2][k]
                        if r1-1 >= 0:
                            m[k] -= s[r1-1][c2][k]
                            if c1-1 >= 0:
                                m[k] += s[r1-1][c1-1][k]
                        if c1-1 >= 0:
                            m[k] -= s[r2][c1-1][k]
                        m[k] -= mb[r1][c1][k] + mb[r1][c2][k] + \
                            mb[r2][c1][k] + mb[r2][c2][k]
                    
                    if m[0] >= 0 and (r1+r2)*m[0] == 2*m[1] and \
                                     (c1+c2)*m[0] == 2*m[2]:
                        tm = max(tm, r2-r1+1)
                        
    return "IMPOSSIBLE" if tm < 0 else tm
        
for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
