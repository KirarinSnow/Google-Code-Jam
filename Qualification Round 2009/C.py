#!/usr/bin/python
#
# Problem: Welcome to Code Jam
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out

import sys
from math import *
from string import *



def grab():
    return int(file.readline())

def grabs():
    return map(int,file.readline().split())

def removechars(str, chars):
    return str.translate(maketrans('',''),chars)

def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def next():
    return buffer.pop(0)

def nint():
    return int(next())

def compute():
    wc = 'welcome to code jam'
    counter = map(lambda x: [x,0], wc)
    s = file.readline()[:-1]

    for c in s:
        if c == 'w':
            counter[0][1]+=1
        for i in range(1,len(counter)):
            if c == counter[i][0]:
                counter[i][1]+=counter[i-1][1]
                counter[i][1]%=10000
    return "%04d" % counter[-1][1]

file = sys.stdin

case = int(file.readline())

for i in range(case):

    print "Case #" + str(i+1) + ":",
    print compute()
