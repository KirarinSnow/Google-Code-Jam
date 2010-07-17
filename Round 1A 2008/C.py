#!/usr/bin/python
#
# Problem: Numbers
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Inefficient algorithm. Does not finish on large set.


from math import *

def compute():
    def mul(x):
	xx = x
	bn = bin(x)[2:][::-1]
        p = [1,0,0,1]
        for i in range(len(bn)):
	    if bn[i] == '1':
		pp = t[i]
		p = [(p[0]*pp[0]+p[1]*pp[2]),
                     (p[0]*pp[1]+p[1]*pp[3]),
                     (p[2]*pp[0]+p[3]*pp[2]),
                     (p[2]*pp[1]+p[3]*pp[3])]
	return p
            
    n = input()
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
    out = (m[0]*3 + m[1])%1000
    o = m[2]*3 + m[3]
    out += int(ceil(o*sqrt(5))) - 1
    return out%1000

for i in range(input()):
    print "Case #%d: %03d" % (i+1, compute())
