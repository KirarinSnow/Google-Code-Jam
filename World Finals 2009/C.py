#!/usr/bin/python
#
# Problem: Doubly-sorted Grid
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Times out on large.


MOD = 10007

def compute():
    def proc(p, k):
        if (p, k) not in pd:
            pp = p
            x = C
            y = 0
            z = -1
            while x > k:
                if pp%2 == 0:
                    x -= 1
                else:
                    z += 1
                y += 1
                pp /= 2
            infl = (y >= 2 and ((p%(1<<y))>>(y-2)) == 1)
            flip = (pp << y) + (2 << (y-2)) + (p%(1<<(y-2))) if infl else None
            pd[(p, k)] = (infl, z, flip)
        return pd[(p, k)]


    def dp(p, c, k):
        if (p, c, k) not in d:
            t = 0
            if p == ((1<<R)-1)<<C:
                t = 1
            else:
                if k == -1:
                    if c != ord('a'):
                        t += dp(p, c-1, C-1)
                        
                else:
                    t += dp(p, c, k-1)
                    infl, row, flip = proc(p, k)
                    
                    if infl:
                        ch = g[row][k]
                        if ch == '.' or ch == chr(c):
                            t += dp(flip, c, k)
            d[(p, c, k)] = t%MOD
        return d[(p, c, k)]

    d = {}
    pd = {}
    R, C = map(int, raw_input().split())
    g = [raw_input() for j in range(R)]

    return dp((1<<R)-1, ord('z'), C-1)
 
for i in range(int(raw_input())):
    print "Case #%d: %d" % (i+1, compute())
