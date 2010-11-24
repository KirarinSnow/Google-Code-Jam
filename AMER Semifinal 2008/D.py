#!/usr/bin/env python
#
# Problem: King
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Adapted from reference solution. Times out on large.


def compute():
    def solve(x, y, b):
        if x == c:
            x = 0
            y += 1
            if y == r: return 0
    
        if m[x][y][b] != -1:
            return m[x][y][b]

        bb = (b<<1) & ((1<<(c+1))-1)
    
        if a[y][x] != '.':
            m[x][y][b] = solve(x+1, y, bb)
        else:
            m[x][y][b] = solve(x+1, y, bb+1)
            if x and b&1:
                m[x][y][b] = max(m[x][y][b], 1+solve(x+1, y, bb-2))
            if x and b&(1<<c):
                m[x][y][b] = max(m[x][y][b], 1+solve(x+1, y, bb))
            if b&(1<<(c-1)):
                m[x][y][b] = max(m[x][y][b], 1+solve(x+1, y, bb-(1<<c)))
            if x < c-1 and b&(1<<(c-2)):
                m[x][y][b] = max(m[x][y][b], 1+solve(x+1, y, bb-(1<<(c-1))))
        return m[x][y][b]

    r, c = map(int, raw_input().split())
    a = [raw_input() for i in range(r)]
    
    m = [[[-1] * (1<<16) for i in range(r)] for j in range(c)]
    m1 = solve(0, 0, 0)
    a = map(lambda y: ''.join(map(lambda x: (x=='K' and '.') or x, y)), a)
    m = [[[-1] * (1<<16) for i in range(r)] for j in range(c)]
    m2 = solve(0, 0, 0)
    
    if m2 > m1:
        return "A"
    else:
        return "B"

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
