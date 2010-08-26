#!/usr/bin/env python
#
# Problem: Apocalypse Soon
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


import copy

def compute():
    
    def advance(board, d):
        board2 = copy.deepcopy(board)
        for x in range(R):
            for y in range(C):
                if board[x][y] > 0:
                    target = None
                    m = 0
                    if (x, y) != (r, c):
                        for n in nb[x][y]:
                            if board[n[0]][n[1]] > m:
                                m = board[n[0]][n[1]]
                                target = n
                    if target != None:
                        board2[target[0]][target[1]] -= board[x][y]

        return board2
        
    def neighbors(x, y):
        ret = []
        for i, j in [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]:
            if 0 <= i < R and 0 <= j < C:
                ret.append((i, j))
        return ret

    C, R, c, r = map(int, raw_input().split())
    r -= 1
    c -= 1
    board = [map(int, raw_input().split()) for i in range(R)]

    nb = [[neighbors(x, y) for y in range(C)] for x in range(R)]
    
    
    dirs = [d for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if (r+d[0], c+d[1]) in nb[r][c]]

    mdays = 0
    queue = [(board, 0)]
    
    while queue:
        b, days = queue.pop()

        if b[r][c] > 0:
            mdays = max(mdays, days)

            if len(filter(lambda n: b[n[0]][n[1]] > 0, nb[r][c])) == 0:
                return "forever"

            b2 = advance(b, d)
            queue.append((b2, days+1))

            for d in dirs:
                if b2[r+d[0]][c+d[1]] > 0:
                    b3 = copy.deepcopy(b2)
                    b3[r+d[0]][c+d[1]] -= b[r][c]                
                    queue.append((b3, days+1))

    return "%d day(s)" % mdays
    

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
