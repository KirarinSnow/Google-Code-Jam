#!/usr/bin/python
#
# Problem: Crop Triangles
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out
# Comments: Inefficient brute-force approach. Does not finish on large set.

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
    n, a, b, c, d, x0, y0, m = map(int,file.readline().split())
    pts = []
    x = x0
    y = y0
    pts.append([x0,y0])
    for i in range(1,n):
	x = (a*x+b)%m
	y = (c*y+d)%m
	pts.append([x,y])
    c = 0

    for i in range(len(pts)):
	for j in range(i+1,len(pts)):
	    for k in range(j+1,len(pts)):
		if (pts[i][0]+pts[j][0]+pts[k][0])%3 == 0 and (pts[i][1]+pts[j][1]+pts[k][1])%3 == 0:
		    c+=1
    return str(c)

file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
