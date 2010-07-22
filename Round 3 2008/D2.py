#!/usr/bin/python
#
# Problem: Endless Knight
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Unified solution. Works for both small and large.


from itertools import *

MOD = 10007
CUTOFF = 100

# Precompute factorial table mod MOD
fact = [1] * MOD
for i in xrange(1, MOD):
    fact[i] = (fact[i-1] * i) 

# n choose k -- using Lucas's theorem
def choose(n, k):
    if k > n:
        return 0
    elif n < MOD:
        return (fact[n]/fact[n-k]/fact[k])%MOD
    else:
        prod = 1
        while n > 0:
            prod *= choose(n%MOD, k%MOD)
            prod %= MOD
            n /= MOD
            k /= MOD
        return prod

def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def compute():
    h, w, r = map(int, raw_input().split())

    if h <= CUTOFF and w <= CUTOFF: # small solution
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

    else: # large solution
        rocks = [map(int, raw_input().split()) for i in range(r)]
    
        if (h+w-2)%3 != 0:
            return 0

        # normalize rock coordinates
        h, w = h-1-(h+w-2)/3, w-1-(h+w-2)/3
        
        for i in range(r):
            row, col = rocks[i]
            if (row+col-2)%3 != 0:
                rocks[i] = None
            else:
                rocks[i] = [row-1-(row+col-2)/3, col-1-(row+col-2)/3]
                if rocks[i][0] < 0 or rocks[i][0] > h:
                    rocks[i] = None
                elif rocks[i][1] < 0 or rocks[i][1] > w:
                    rocks[i] = None
        
    
        total = 0
        for num in range(r+1):
            for perm in permutations(range(r), num):

                # verify increasing property of permutation
                inc = True
                for i in range(num):
                    if rocks[perm[i]] == None:
                        inc = False
                        break
                    if i > 0:
                        if rocks[perm[i]][0] < rocks[perm[i-1]][0]:
                            inc = False
                            break
                        if rocks[perm[i]][1] < rocks[perm[i-1]][1]:
                            inc = False
                            break

                if inc:
                    points = [[0,0]] + [rocks[j] for j in perm] + [[h,w]]
                    
                    # number of paths going through all points
                    prod = 1
                    for j in range(1, len(points)):
                        dh = points[j][0] - points[j-1][0]
                        dw = points[j][1] - points[j-1][1]
                        prod *= choose(dh+dw, dw)
                        prod %= MOD
                        
                    # inclusion-exclusion
                    total += (-1)**num * prod
                    total %= MOD
        
        return total


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
