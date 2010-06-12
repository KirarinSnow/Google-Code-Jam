#!/usr/bin/python
#
# Problem: PermRLE
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

# from http://snippets.dzone.com/posts/show/753
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def compute():

    def ct(ii):
	ctt = 0
	tabl[ii].append(0)
	for r in range(len(tabl[0])-1):
	    if tabl[ii][r]!=tabl[ii][r+1]:
		ctt+=1
	return ctt

    k = grab()
    ss = removechars(file.readline(),'\n')
    ll = len(ss)
    nn = ll/k
    ps = []
    for j in all_perms(range(k)):
	ps.append(j)

    tabl = []
    for i in range(len(ps)):
	tabl.append([])
	perm = ps[i]
	for j in range(nn):
	    subs = ss[j*k:j*k+k]
	    for jj in range(k):
		tabl[i].append(subs[perm[jj]])

    cc = 1000000000000

    x = len(ps)
    for i in range(x):
	cc = min(cc,ct(i))

    return str(cc)


file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
