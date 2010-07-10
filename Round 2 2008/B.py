#!/usr/bin/python
#
# Problem: Triangle Areas
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Inefficient brute-force solution. 


from math import *

def compute():
    n, m, a = map(int, raw_input().split())

    xa = 0
    ya = 0
    for xb in range(0, n+1):
	if xb == 0:
	    v = 0
	else:
	    v = a/xb
	for yc in range(v, m+1):
	    bc = xb * yc - a
	    xc = 0
	    yb = 0
	    if bc == 0:
		xc = 0
		yb = 0
	    else:
		for k in range(1, int(sqrt(max(0,bc)))+1): 
		    if bc % k == 0 and bc/k <= n and k <= m:
			xc = bc/k
			yb = k
			break

	    if xb*yc-xc*yb == a:
                return ' '.join(map(str, [xa, ya, xb, yb, xc, yc]))


    return "IMPOSSIBLE"

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
