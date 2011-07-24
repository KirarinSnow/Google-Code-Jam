#!/usr/bin/python
#
# Problem: EZ-Sokoban
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    def safe(u):
        c = 1
        qq = [u[0]]
        ss = set()
        while qq:
            v = qq.pop(0)
            if v not in ss:
                ss.add(v)
                for n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next = (v[0]+n[0], v[1]+n[1])
                    if next in u:
                        qq.append(next)
        return len(ss) == len(u)

    r, c = map(int, raw_input().split())
    b = [raw_input() for i in range(r)]

    init = []
    final = []
    for i in range(r):
        for j in range(c):
            if b[i][j] in 'ow':
                init.append((i, j))
            if b[i][j] in 'xw':
                final.append((i, j))
    init = tuple(init)
    final = tuple(final)

    q = [[0, 0, init]]
    s = set()
    while q:
        d, h, u = q.pop(0)
        if u == final:
            return d
        if safe(u):
            h = 0
        else:
            h += 1
        if len(u) > 1 and h > 1:
            continue
        if u not in s:
            s.add(u)
            for y, x in enumerate(u):
                for n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    f = (x[0]+n[0], x[1]+n[1])
                    t = (x[0]-n[0], x[1]-n[1])
                    if 0 <= f[0] < r and 0 <= f[1] < c and \
                            0 <= t[0] < r and 0 <= t[1] < c and \
                            b[f[0]][f[1]] != '#' and \
                            b[t[0]][t[1]] != '#' and \
                            (f not in u) and (t not in u):
                        l = u[:y] + u[y+1:] + (t,)
                        q.append([d+1, h, tuple(sorted(l))])
                            
    return -1

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
