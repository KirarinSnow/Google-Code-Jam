#!/usr/bin/python
#
# Problem: Increasing Speed Limits
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Fails on large set.


MOD = 1000000007

def compute():
    n, m, x, y, z = map(int, raw_input().split())
    a = []
    for i in range(m):
        a.append(input())
    
    s = []
    for i in range(n):
        s.append(a[i%m])
        a[i%m] = (x*a[i%m] + y*(i+1))%z
    
    f = [1]*n
    for i in range(n)[::-1]:
        for j in range(i,n):
            if s[i] < s[j]:
                f[i]+=f[j]
                f[i]%=MOD
    return sum(f)%MOD
    

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
