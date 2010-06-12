#!/usr/bin/python
#
# Problem: How Big Are the Pockets?
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

def table(height, width):
    t = []
    for i in range(height):
	t.append([])
	for j in range(width):
	    t[i].append(0)
    return t

def compute():
    def adv(x,y,o):
        if o==0:
            if y not in d:
                d[y] = []
            d[y].append(x)
            return (x,y+1,o)
        elif o==1:
            if x not in e:
                e[x] = []
            e[x].append(y)
            return (x+1,y,o)
        elif o==2:
            if y-1 not in d:
                d[y-1] = []
            d[y-1].append(x)
            return (x,y-1,o)
        else:
            if x-1 not in e:
                e[x-1] = []
            e[x-1].append(y)
            return (x-1,y,o)

    def left(x,y,o):
        return (x,y,(o-1)%4)
    def right(x,y,o):
        return (x,y,(o+1)%4)

    l = int(buffer.pop(0))
    cur = ""
    for i in range(l):
        st = buffer.pop(0)
        count = int(buffer.pop(0))
        cur += (count * st)

    x,y,o = 0,0,0

    d = dict()
    e = dict()

    for s in cur:
        if s == 'F':
            x,y,o = adv(x,y,o)
        elif s == 'L':
            x,y,o = left(x,y,o)
        else:
            x,y,o = right(x,y,o)
 
    sum = 0
    for k in d:
        d[k].sort()
        v = d[k][1:-1]
        for i in range(len(v)/2):
            sum += v[2*i+1]-v[2*i]

    for k in e:
        e[k].sort()
        u = e[k][1:-1]
        for i in range(len(u)/2):
            
            for j in range(u[2*i], u[2*i+1]):
                mn,mx = d[j][0], d[j][-1]
                if k < mn or k >= mx:
                    sum += 1

    return sum
            

file = sys.stdin

n = int(file.readline())
buffer = file.read().split()

for i in range(n):

    print "Case #" + str(i+1) + ":",
    print compute()
