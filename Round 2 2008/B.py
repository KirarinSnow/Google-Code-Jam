#!/usr/bin/python
#
# Problem: Triangle Areas
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out
# Comments: Inefficient brute-force solution. 

import sys
from math import *
from string import *

MAX = 100000000000


def grab():
    return int(file.readline())

def grabs():
    return map(int,file.readline().split())

def removechars(str, chars):
    return str.translate(maketrans('',''),chars)

def compute():
    n,m,a = grabs()

    ssss = ""
    xa = 0
    ya = 0
    for xb in range(0,n+1):
	if xb == 0:
	    v = 0
	else:
	    v = a/xb
	for yc in range(v,m+1):
	    bc = xb * yc - a
	    xc = 0
	    yb = 0
	    if bc == 0:
		xc = 0
		yb = 0
	    else:
		for k in range(1,int(sqrt(bc)+1)): 
		    if bc % k == 0 and bc/k <= n and k <= m:
			xc = bc/k
			yb = k
			break

	    if xb*yc-xc*yb == a:
		ssss += str(xa) + " " + str(ya) + " "
		ssss += str(xb) + " " + str(yb) + " "
		ssss += str(xc) + " " +  str(yc)
		return ssss

    return "IMPOSSIBLE"

file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
