#!/usr/bin/env python
#
# Problem: Minesweeper Master
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    r, c, m = map(int, raw_input().split())
    
    transpose = False
    if r > c:
        transpose = True
        r, c = c, r

    f = [['*']*c for i in range(r)]
    v = r*c-m

    possible = True
    if v == 0:  # always impossible if no room
        possible = False
    elif v == 1:  # always ok if only one spot without mine
        f[0][0] = '.'
    else:
        if r == 1:  # always ok for one row/column
            for i in range(v):
                f[0][i] = '.'
        elif r == 2:  # ok for even numbers of spots >= 4
            if v%2 == 0 and v >= 4:
                for i in range(v/2):
                    f[0][i] = f[1][i] = '.'
            else:
                possible = False
        else:  # ok for 4, 6, and 8+ spots
            if v == 4 or v == 6:
                for i in range(v/2):
                    for j in range(2):
                        f[i][j] = '.'
            elif v <= 7:
                possible = False
            else:
                if v <= 2*c+3: # fill top left 3x2 rectangle, then
                               # pairs of cells in top 2 rows, and fill out
                               # top left 3x3 if needed
                    for j in range(v/2-1):
                        f[0][j] = f[1][j] = '.'
                    f[2][0] = f[2][1] = '.'
                    if v%2 == 1:
                        f[2][2] = '.'
                else: # just fill in rows completely from top left
                    for i in range(v):
                        f[i/c][i%c] = '.'
                    if v%c == 1:  # except if that leaves a stranded spot at
                                  # the beginning of a new row, in which case
                                  # the last cell should be filled with a mine
                                  # and there should be two spots at the
                                  # beginning of the new row
                        f[v/c][1] = '.'
                        f[v/c-1][c-1] = '*'
                        
    if possible:
        f[0][0] = 'c'
        if transpose:
            f = zip(*f)
        out = '\n'.join(map(lambda x: ''.join(x), f))
    else:
        out = "Impossible"
    print "Case #%d:\n%s" % (case+1, out)
