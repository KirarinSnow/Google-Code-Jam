#!/usr/bin/python
#
# Problem: Numbers
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out
# Comments: Inefficient algorithm. Does not finish on large set.

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

def h2b(s):
    oo = ""
    for ii in s:
        if ord(ii) >= ord('0') and ord(ii) <= ord('9'):
            j = (ord(ii)-ord('0'))
        else:
            if ord(ii.lower()) >= ord('a') and ord(ii.lower()) <= ord('f'):
                j = (ord(ii.lower())-ord('a') + 10)
        for v in range(4):
            if j/2**(3-v) % 2 == 1:
                oo += '1'
            else:
                oo += '0'
    return oo

def h2d(s):
    return b2d(h2b(s))

def d2b(s):
    return h2b(d2h(s))

def d2h(n):
    k = hex(n)
    return k[2:len(k)]

def b2h(s):
    return d2h(b2d(s))

def b2d(s):
    kk = 0
    for i in range(len(s)):
        j = len(s) - 1 - i
        if s[j] == '1':
            kk += 2**i
    return kk



def compute():
    def mul(x):
	xx = x
	bn = d2b(x)
	p = [1,0,0,1]
	for i in range(len(bn)):
	    if bn[::-1][i] == '1':
		pp = t[i]
		p = [(p[0]*pp[0]+p[1]*pp[2]),(p[0]*pp[1]+p[1]*pp[3]),(p[2]*pp[0]+p[3]*pp[2]),(p[2]*pp[1]+p[3]*pp[3])]

	return p
            
    n = grab()
    a, b, c, d = 3, 5, 1, 3
    
    
    t = [[a,b,c,d]]
    e = int(floor(log(n)/log(2))) + 1
    for i in range(e):
	aa = t[i][0]
	bb = t[i][1]
	cc = t[i][2]
	dd = t[i][3]
	
	aaa = aa*aa + bb*cc
	bbb = aa*bb + bb*dd
	ccc = cc*aa + dd*cc
	ddd = cc*bb + dd*dd
	t.append([aaa,bbb,ccc,ddd])
    
    m = mul(n-1)
    out = ((m[0]*3)+m[1])%1000
    o = (m[2]*3+m[3])
    out += int(ceil(o*sqrt(5))) -1
    return str(1000+(out%1000))[1:4]
    

file = sys.stdin

n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s+= compute()
    print s
