#!/usr/bin/env python
#
# Problem: De-RNG-ed
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from math import sqrt

MAX = 10**6
prime = [True]*(MAX+1)
for n in xrange(2,int(sqrt(MAX))+1):
    for i in xrange(2*n, MAX+1, n):
        prime[i] = False
primes = []
for n in range(2, len(prime)):
    if prime[n]:
        primes.append(n)

for case in range(int(raw_input())):
    d, k = map(int, raw_input().split())
    s = map(int, raw_input().split())
    
    u = "I don't know."
    if k == 1 or (k == 2 and s[0] != s[1]):
        ans = u
    elif s[-1] == s[-2]:
        ans = s[-1]
    else:
        c = []
        for p in primes:
            if p <= max(s):
                continue
            if p > 10**d:
                break
            x, y, z = s[:3]
            a = (z-y)*pow(y-x, p-2, p)%p
            b = (y-a*x)%p
            w = s[0]
            for v in s[1:]:
                if (a*w+b)%p != v:
                    break
                w = v
            else:
                c.append((a*s[-1]+b)%p)

        if len(set(c)) == 1:
            ans = c[0]
        else:
            ans = u

    print "Case #%d: %s" % (case+1, ans)
