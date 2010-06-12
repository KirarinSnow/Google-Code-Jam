#!/usr/bin/python
#
# Problem: Text Messaging Outrage
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
    p,k,l = grabs()
    fs = grabs()
    
    fs.sort()

    c = 0
    for i in range(l):
	c+=fs[l-i-1] * (i/k + 1)

    return str(c)

file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
