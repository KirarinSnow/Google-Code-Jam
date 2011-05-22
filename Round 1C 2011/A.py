#!/usr/bin/python
#
# Problem: Square Tiles
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    r, c = map(int, raw_input().split())
    g = [list(raw_input()) for i in range(r)]
    for i in range(r-1):
        for j in range(c-1):
            if g[i][j] == g[i+1][j] == g[i][j+1] == g[i+1][j+1] == '#':
                g[i][j] = g[i+1][j+1] = '/'
                g[i+1][j] = g[i][j+1] = '\\'
    if len(filter(lambda x: filter(lambda y: y == '#', x), g)) > 0:
        print "Impossible"
    else:
        print '\n'.join(map(lambda x: ''.join(x), g))

                
for i in range(input()):
    print "Case #%d:" % (i+1)
    compute()
