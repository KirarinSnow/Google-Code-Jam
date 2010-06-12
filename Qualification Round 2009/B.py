#!/usr/bin/env python
#
# Problem: Watersheds
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

    def nxt(sink):
        r, c = sink
        mn = mp[r][c]
        dest = False
        if (r>0 and mp[r-1][c]<mn):
            mn = mp[r-1][c]
            dest = (r-1,c)
        if (c>0 and mp[r][c-1]<mn):
            mn = mp[r][c-1]
            dest = (r,c-1)
        if (c<w-1 and mp[r][c+1]<mn):
            mn = mp[r][c+1]
            dest = (r,c+1)
        if (r<h-1 and mp[r+1][c]<mn):
            mn = mp[r+1][c]
            dest = (r+1,c)
        return dest

    def label(sink, lt):
        q = [sink]
        while q:
            r,c = q.pop(0)
            if out[r][c] == 0:
                out[r][c] = lt
                if (r>0 and nxt((r-1,c)) == (r,c)):
                    q.append((r-1,c))
                if (c>0 and nxt((r,c-1)) == (r,c)):
                    q.append((r,c-1))
                if (c<w-1 and nxt((r,c+1)) == (r,c)):
                    q.append((r,c+1))
                if (r<h-1 and nxt((r+1,c)) == (r,c)):
                    q.append((r+1,c))
            

    h, w = nint(), nint()
    mp = table(h, w)
    for i in range(h):
        for j in range(w):
            mp[i][j] = nint()

    out = table(h, w)

    lt = 97
    for r in range(h):
        for c in range(w):
            if out[r][c] == 0:
                # find sink
                sink = (r,c)
                while nxt(sink):
                    sink = nxt(sink)
                # BFS
                label(sink,lt)
                lt += 1
    
    print
    for r in range(h):
        for c in range(w):
            print chr(min(122,out[r][c])),
        print
    

file = sys.stdin

case = int(file.readline())
buffer = file.read().split()

for i in range(case):

    print "Case #" + str(i+1) + ":",
    compute()
