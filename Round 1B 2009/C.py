#!/usr/bin/python
#
# Problem: Square Math
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: May take too long on large.


def compute():
    w, q = map(int, raw_input().split())
    b = [raw_input() for i in range(w)]
    qs = map(int, raw_input().split())
    qss = set(qs)
    a = {}
    h = 1<<30
    cs = len(qss)
    
    s = {}
    r = []
    d = {}
    for i in range(w):
        for j in range(w):
            if ord(b[i][j]) >= 48:
                d[(i, j, int(b[i][j]))] = b[i][j]
                r.append((i, j, int(b[i][j])))
    while r:
        i, j, v = r.pop(0)
        if len(d[(i, j, v)]) > h:
            break

        if (i, j, v) in s:
            continue
        s[(i, j, v)] = True
        if v in qss:
            if v in a:
                if len(d[(i, j, v)]) <= len(a[v]) and d[(i, j, v)] <= a[v]:
                    a[v] = d[(i, j, v)]
            else:
                a[v] = d[(i, j, v)]
            if len(a) == cs:
                h = len(d[(i, j, v)])

        for x1, y1 in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            for x2, y2 in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ii = i+x1+x2
                jj = j+y1+y2
                if 0 <= i+x1 < w and 0 <= j+y1 < w and \
                        0 <= ii < w and 0 <= jj < w:                   
                    e = d[(i, j, v)]+b[i+x1][j+y1]+b[ii][jj]

                    if b[i+x1][j+y1] == '-':
                        c = v - (ord(b[ii][jj])-48)
                    else:
                        c = v + (ord(b[ii][jj])-48)

                    if (ii, jj, c) in d:
                        if len(e) <= len(d[(ii, jj, c)]) and e < d[(ii, jj, c)]:
                            d[(ii, jj, c)] = e
                    else:
                        d[(ii, jj, c)] = e
                    r.append((ii, jj, c))

    for c in qs:
        print a[c]
    
    
for i in range(input()):
    print "Case #%d:" % (i+1)
    compute()
