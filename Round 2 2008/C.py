#!/usr/bin/python
#
# Problem: Star Wars
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out



MAX = 10**7
CUTOFF = 1e-7


def test(P, ships):
    # initial range for each of four intervals constraining X, Y, Z
    # p = +; m = -; x +/- y +/- z
    ppmax = MAX
    ppmin = -MAX
    pmmax = MAX
    pmmin = -MAX
    mpmax = MAX
    mpmin = -MAX
    mmmax = MAX
    mmmin = -MAX
    
    # compute intersection over all ships
    for s in ships:
        x, y, z, p = s
        ppmax = min(ppmax, P*p+x+y+z)
        ppmin = max(ppmin, -P*p+x+y+z)
        pmmax = min(pmmax, P*p+x+y-z)
        pmmin = max(pmmin, -P*p+x+y-z)
        mpmax = min(mpmax, P*p+x-y+z)
        mpmin = max(mpmin, -P*p+x-y+z)
        mmmax = min(mmmax, P*p+x-y-z)
        mmmin = max(mmmin, -P*p+x-y-z)

    # boundary conditions do not intersect: no solution
    if ppmin>ppmax or pmmin>pmmax or mpmin>mpmax or mmmin>mmmax:
        return False
    
    # determine if remaining four intervals are consistent
    if max(pmmin+mpmin, ppmin+mmmin) > min(pmmax+mpmax, ppmax+mmmax):
        return False

    return True
    


def compute():
    n = input()
    ships = []
    for i in range(n):
        ships.append(map(int, raw_input().split()))

    # binary search on P, power of cruiser
    l = 0
    u = MAX*3
    while u-l > CUTOFF:
        m = (l+u)/2.0
        if test(m, ships):
            u = m
        else:
            l = m
    
    return l


for i in range(input()):
    print "Case #%d: %0.6f" % (i+1, compute())
