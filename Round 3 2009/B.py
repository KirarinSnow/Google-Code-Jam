#!/usr/bin/python
#
# Problem: Alphabetomials
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from itertools import *


MOD = 10009

def compute():
    def f(k, m):
        if (k, m) not in mem:
            if len(m) == 0:
                out = pow(n, k, MOD)
            else:
                out = 0
                if k > 0:
                    for t in xrange(1 << len(m)):
                        c = [x for i, x in enumerate(m) if t & (1 << i)]
                        r = [x for i, x in enumerate(m) if not t & (1 << i)]

                        s = 0
                        for j in range(n):
                            pr = 1
                            for a in c:
                                pr *= fr[a][j]
                                pr %= MOD
                            s += pr
                            s %= MOD
                        out += s*f(k-1, ''.join(r))
                        out %= MOD
            mem[(k, m)] = out
        return mem[(k, m)]
                
        
    poly, k = raw_input().split()
    k = int(k)
    n = input()
    w = [raw_input() for i in range(n)]
    fr = {}
    mem = {}
    for ch in map(chr, range(97, 123)):
        fr[ch] = map(lambda x: x.count(ch), w)
    
    ps = poly.split('+')
    
    out = [0]*k


    for d in range(1, k+1):
        for m in ps:
            out[d-1] += f(d, m)
            out[d-1] %= MOD

    return ' '.join(map(str, out))
        

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
