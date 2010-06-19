#!/usr/bin/python
#
# Problem: Mousetrap
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out
# Comments: Fails on large set.


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
    k = grab()
    r = grabs()
    n = r.pop(0)
    sn = range(k)
    a = [0]*k
    c = 0
    i = 1
    cc = 0
    p=0
    d3ex = range(k)
    dex = sorted(d3ex)
    while i <=k:
	rd = k-i+1
	
	v = (p+i-1)%rd
	a[dex[v]] = i
	p = dex.index(dex[v])
	del dex[v]
	i = i+1

    s = ""
    for j in r:
	s += str(a[j-1]) + " "
    return s

file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
