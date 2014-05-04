#!/usr/bin/env python
#
# Problem: Different Sum
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Takes too long on the large input.


from math import *

MOD = 1000000007

MAXB = 70
ch = [[0]*(MAXB+1) for ii in range(MAXB+1)]
ch[0][0] = 1
for i in range(MAXB+1):
    ch[i][0] = 1
    ch[i][i] = 1
    for j in range(1, i):
        ch[i][j] = ch[i-1][j-1]+ch[i-1][j]
        ch[i][j] %= MOD

fact = [0]*(MAXB+1)
fact[0] = 1
for i in range(1, MAXB+1):
    fact[i] = fact[i-1]*i
    fact[i] %= MOD


for case in range(int(raw_input())):
    n, b = map(int, raw_input().split())
    
    mb = b*(b-1)/2
    w = 1+int(log(n)/log(b))
    
    # compute count2 table
    d = [[[0 for i in range(mb+1)] for j in range(b+1)] for k in range(b)]
    d[0][0][0] = 1
    for new in range(1, b):
        for np in range(new):
            for k in range(np+1):
                for s in range(min(np*(np+1)/2+1, mb-new+1)):
                    d[new][k+1][s+new] += d[np][k][s]
                    d[new][k+1][s+new] %= MOD

    c2 = [[0 for i in range(b*b+1)] for j in range(b+1)]
    for k in range(b+1):
        for s in range(mb+1):
            for new in range(b):
                c2[k][s] += d[new][k][s]
                c2[k][s] %= MOD

    # compute main DP
    c = [[[[0]*2 for i in range(b+1)] for j in range(b)] for k in range(w+1)]
    for k in range(b+1):
        c[0][0][k][0] = 1
    for i in range(w):
        z = n/b**i%b
        for k in range(b+1):
            for v in range(b):
                for v2 in range(b):
                    if v2 >= mb:
                        continue
                    s = v2*b+z-v
                    
                    if i == 0:
                        for g in range(2):
                            if k-g >= 0:
                                c[i+1][v2][k][g] += c[i][v][k][0]*c2[k-g][s]
                                c[i+1][v2][k][g] %= MOD
                        continue

                    for p in range(k+1):
                        t = 0
                        for f in range(2):
                            if p-f >= 0:
                                t += c[i][v][k][f]*ch[k-f][p-f]
                                t %= MOD

                        for g in range(2):
                            if p-g >= 0:
                                c[i+1][v2][p][g] += t*fact[p]*c2[p-g][s]
                                c[i+1][v2][p][g] %= MOD
                    
    ans = sum(c[w][0][i][0] for i in range(b+1))%MOD
    print "Case #%d: %s" % (case+1, ans)
