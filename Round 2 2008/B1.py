#!/usr/bin/python
#
# Problem: Triangle Areas
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
    n,m,a = grabs()

    if a > n*m:
	return "IMPOSSIBLE"
    else:
	x = (a-1)%n+1
	y = (a-1)/n+1
	ss = "0 1 "
	ss += str(n) + " 0 " + str(x) + " " + str(y)
	return ss

file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
