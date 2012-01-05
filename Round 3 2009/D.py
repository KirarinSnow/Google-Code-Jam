#!/usr/bin/python
#
# Problem: Interesting Ranges
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def nd(x):
    if x <= 0:
        return 0
    else:
        return 1+nd(x/10)

def tot(n):
    if n == 0:
        return 0
    elif n == 1:
        return 5
    elif n == 2:
        return 45
    else:
        p = 9*10**((n+1)/2-1)  
        return m(n)*p/2

def m(n):
    return ((n+1)%2*10 + 1) * 10**((n-1)/2)

def count(l, r):
    return ct(r) - ct(l-1)

def ct(x):
    t = 0
    for i in range(nd(x)):
        t += tot(i)
    t += cd(x)
    return t

def cd(x):
    n = nd(x)
    if n == 0:
        return 0
    elif n == 1:
        return (x+1)/2
    elif n == 2:
        return 1 + (x%11+1)*((x/11-1)%2) + 11*((x/11-1)/2)
    else:
        return ca(x)
           
def ca(x):
    n = nd(x)
    s = str(x)[:(n+1)/2]
    c = int(s + s[::-1][n%2:])
    if x < c:
        s = str(int(s)-1)
        c = int(s + s[::-1][n%2:])
    p = int(s)   
    q = 10**((n-1)/2)
    b = (p-q+1)/2*m(n)
    if x >= c and p%2 == 0:
        b += (x-c)+1
    return b
        
def compute():
    l, r = map(int, raw_input().split())
    z = count(l-1, r)
    o = r-l+2-z
    return (z*(z-1)/2 + o*(o-1)/2)%1000000007

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
