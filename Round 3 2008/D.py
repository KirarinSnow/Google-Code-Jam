#!/usr/bin/python
#
# Problem: Endless Knight
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: OK for small, but times out on large.


def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def compute():
    h, w, r = map(int, raw_input().split())

    rocks = table(h, w)
    board = table(h, w)
    
    for i in range(r):
	rr, cc = map(int, raw_input().split())
	rocks[rr-1][cc-1] = 1
    
    board[0][0] = 1
    for i in range(h):
	for j in range(w):
	    if rocks[i][j] != 1:
		if i-2 >= 0 and j-1 >= 0:
		    board[i][j] += (board[i-2][j-1])
		    board[i][j] %= 10007
		if i-1 >= 0 and j-2 >= 0:
		    board[i][j] += (board[i-1][j-2])
		    board[i][j] %= 10007

    return board[h-1][w-1]


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
