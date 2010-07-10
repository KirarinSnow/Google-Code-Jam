#!/usr/bin/python
#
# Problem: No Cheating
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    def dfs(node): # search for available match
        x, y = node

        if visited[x][y] != label: # not yet seen
            visited[x][y] = label
            for i in [x-1, x, x+1]: # adjacent rows
                for j in [y-1, y+1]: # adjacent cols
                    if 0<=i<m and 0<=j<n and board[i][j] == '.': # in range
                        if match[i][j] == None or dfs(match[i][j]):
                            match[x][y] = (i,j)
                            match[i][j] = (x,y)
                            return True
        return False

    m, n = map(int, raw_input().split())

    board = [list(raw_input()) for i in range(m)]

    match = [[None] * n for i in range(m)]
    visited = [[None] * n for i in range(m)]
    
    vcount = 0
    matching = 0

    label = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == '.':
                vcount += 1
                if j%2 == 1: # odd columns
                    if dfs((i,j)):
                        matching += 1
                    label += 1

    return vcount - matching

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
