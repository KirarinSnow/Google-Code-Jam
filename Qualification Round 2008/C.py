#!/usr/bin/python
#
# Problem: Fly Swatter
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Inefficient O(n^2)-time algorithm. Can be done in O(n) time.
#           Large set: 11m51.719s


import sys
import math

MAX = 1000000000

file = sys.stdin

def ar(x1,x2,y,r):
    def integ(x):
        if x > 1: x = 1.0
        return 0.5 * math.asin(x) + 0.5 * x * math.sqrt(1.0 - x*x)

    return r*r * (integ((x2+0.0)/r) - integ((x1+0.0)/r)) - y * (x2-x1)

def prob():
    f, rr, t, r, g = map(float,file.readline().split())

    if 2*f > g:
	return "1"

    total = math.pi * rr**2 / 4.0

    count = 0.0
    ro = rr-t-f
    ltt = g - 2*f
    area = ltt**2

    x = r+f
    while (x < ro):
	y = r + f
	while (y < ro):
	    xx = x + ltt
	    yy = y + ltt
	    p = math.sqrt(x**2 + y**2)
	    q = math.sqrt(xx**2 + yy**2)
	    
	    if p >= rr-t-f:
		count += 0
	    else:
		if q <= rr-t-f:
		    count += area
		else:
		    ty = math.sqrt(ro*ro - x*x)
		    tyy = math.sqrt(max(0,ro*ro - xx*xx))
		    tx = math.sqrt(ro*ro - y*y)
		    txx = math.sqrt(max(0,ro*ro - yy*yy))
		    
		    if (ty < yy):	
			if (tyy > y): #A
			    count += ar(x,xx,y,ro)

			else: #B
			    count += ar(x,tx,y,ro)
		    else:
			if (tyy > y): #C
			    count += ar(txx,xx,y,ro) + (yy-y)*(txx-x)
			else: #D
			    count += ar(y,yy,x,ro)

	    y += g + 2*r
	x +=  g + 2*r

    qqq = (total-count)/total
    return str(qqq)


n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s += prob()
    print s
