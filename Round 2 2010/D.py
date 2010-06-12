#!/usr/bin/python
#
# Problem: Grazing Google Goats
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Requires PARI/GP. Works only on small set.


from math import *
from os import *

def compute(case):
    n, m = map(int, raw_input().split())
    
    p = []
    for i in range(n):
        p.append(map(int, raw_input().split()))

    q = []
    for i in range(m):
        q.append(map(int, raw_input().split()))

    
    # WORKS FOR N = 2 ONLY
    
    # for precision, export to PARI/GP
    ss = "echo \""
    ss += "print(\\\"Case #%d:\\\");"%case
    for i in range(m):
        ss += "r=sqrt((%d- %d)^2+(%d- %d)^2);"%(p[0][1],q[i][1],p[0][0],q[i][0])
        ss += "s=sqrt((%d- %d)^2+(%d- %d)^2);"%(p[1][1],q[i][1],p[1][0],q[i][0])
        ss += "d=sqrt((%d- %d)^2+(%d- %d)^2);"%(p[1][1],p[0][1],p[1][0],p[0][0])
        ss += "print(r*r*acos((d*d+r*r-s*s)/(2*d*r)) + s*s*acos((d*d+s*s-r*r)/(2*d*s)) - 0.5*sqrt((-d+r+s)*(d+r-s)*(d-r+s)*(d+r+s)));"
        
    ss += "\" | gp -f -q | tr '\\n' ' '; echo" 
    system(ss)

for i in range(input()):
    compute(i+1)
