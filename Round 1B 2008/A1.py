#!/usr/bin/python
#
# Problem: Crop Triangles
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out

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

    v = []
    for q in range(3):
	v.append([])
	for r in range(3):
	    v[q].append(0)
    
    for p in pts:
	px = p[0]%3
	py = p[1]%3
	v[px][py] +=1

    for i in range(3):
	for j in range(3):
	    c+= (v[i][j])*(v[i][j]-1)*(v[i][j]-2)/6

    for i in range(3):
	c+= v[i][1]*v[i][2]*v[i][0]
	c+= v[1][i]*v[2][i]*v[0][i]

    for i in range(3):
	c += v[i%3][0] * v[(i+1)%3][1] * v[(i+2)%3][2]
    
    for i in range(3):
	c += v[i%3][0] * v[(i-1)%3][1] * v[(i-2)%3][2]

    return str(c)

file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
