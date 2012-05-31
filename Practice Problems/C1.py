#!/usr/bin/python
#
# Problem: Egg Drop
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


t = []
s = 575
bs = s

for i in range(s+1):
    t.append([])
    for j in range(bs+1):
        t[i].append(0)

for d in range(1, s+1):
    for b in range(1, d+1):
        if b == 1:
            t[d][b] = d
        else:
            if d == b:
                t[d][b] = 2**d - 1
            else:
                t[d][b] = 1 + t[d-1][b-1] + t[d-1][b]

def compf(d, b):
    if b == 1:
	return d
    elif b == 2:
	return cc2(d)
    elif b == 3:
	return cc3(d)
    elif b == 4:
	return cc4(d)
    else:
	if d >= s:
	    return -1
	elif b >= s:
	    return -1
	else:
	    return t[d][b]

def cc2(d):
    return d*(d+1)/2

def cc3(d):
    return (d**3+5*d)/6

def cc4(d):
    d2 = d
    return int((d2-1)**4/24.+(d2-1)**3/12.+(11/24.)*(d2-1)**2+(17/12.)*(d2-1)+1)

def cc(b, d):
    if b == 2:
	return cc2(d)
    if b == 3:
	return cc3(d)
    if b == 4:
	return cc4(d)
    else:
	return d

def factorial(n):
    if n == 0:
	return 1
    else:
	return n * factorial(n-1)

def compd(f, b):
    if b > 4:
	d = 1            
	while d < s:
	    bb = 1
	    while bb <= b:
		if bb > s:
		    break
		if t[d][bb] >= f:
		    return d
		bb += 1
	    d += 1
	return -1
    else:
	if b == 1:
	    return f
	else:
	    dt = int((factorial(b)*(f+1))**(1.0/b)+10)
	    while cc(b, dt) >= f:
		dt -= 1
	    return dt+1

def compb(f, d):
    if (d < s):
	b = 0
	while t[d][b] < f:
	    b += 1
	return b
    else:
	b1 = 4
	while b1 >= 1 and cc(b1, d) > f:
	    b1 -= 1
	return b1 + 1

def reduc(x):
    if x >= 2**32:
	return -1
    else:
	return x


for i in range(input()):
    f, d, b = map(int, raw_input().split())
    
    ff = compf(d, b)
    dd = compd(f, b)
    bb = compb(f, d)
    fff, ddd, bbb = map(reduc, [ff, dd, bb])
    
    print "Case #%d: %d %d %d" % (i+1, fff, ddd, bbb)
