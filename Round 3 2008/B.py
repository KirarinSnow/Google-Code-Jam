#!/usr/bin/python
#
# Problem: Portal
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out
# Comments: Breadth-first search. Extremely slow.

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

    def check(i,j):
        return i >= 0 and j >= 0 and i < r and j < c and room[i][j] != '#' 

    r,c = map(int,file.readline().split())

    room  = []
    for i in range(r):
        room.append(file.readline()[:-1])

    source = -1
    cake = -1
    noportal = [-1,-1]

    for i in range(r):
        for j in range(c):
            if room[i][j] != '#':
                if room[i][j]=='O':
                    source = [[i,j],noportal]
                if room[i][j]=='X':
                    cake = [[i,j],noportal]

    nodes = [[-2,0],source]
    visited = []
    dist = 0

    while (len(nodes)>0):
        
        curren3t = nodes.pop(0)
        
        if curren3t[0] == -2:
            dist = curren3t[1]
            continue

        visited.append(curren3t)
        current = [curren3t[0][0],curren3t[0][1]]
        portal = curren3t[1]

        if current == cake[0]:
            return str(dist)
        ck = [noportal,portal]

        for z in [[0,1],[0,-1],[1,0],[-1,0]]:
            zz = [current[0],current[1]]
            while check(zz[0]+z[0],zz[1]+z[1]):
                zz[0] += z[0]
                zz[1] += z[1]
            if (not (zz in ck)) and zz != current:
                ck.append(zz)
   
        nodes.append([-2,dist+1])
        for z in [[0,1],[0,-1],[1,0],[-1,0]]:
            dest = [z[0]+current[0],z[1]+current[1]]
            if check(dest[0],dest[1]):
                for i in range(len( ck)):
                    if (not ([dest,ck[i]] in visited)) and (not ([dest,ck[i]] in nodes)):
                        nodes.append([dest,ck[i]])

        p = 0
        for z in [[0,1],[0,-1],[1,0],[-1,0]]:
            if not check(z[0]+current[0],z[1]+current[1]):
                p += 1
        if p > 0:
            for i in range(len(ck)):
                if ((not ([ck[i],noportal] in visited)) and (not ([ck[i],noportal] in nodes)) and ck[i] != noportal):
                    nodes.append([ck[i],noportal])

    return "THE CAKE IS A LIE"


file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
