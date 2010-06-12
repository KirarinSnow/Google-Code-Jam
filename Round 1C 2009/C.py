#!/usr/bin/python
#
# Problem: Bribe the Prisoners
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py < input.in > output.out


import sys
from math import *
from string import *


def compute():

    g = dict()

    def gold(x1, x2, r1, r2):
        if (x1,x2,r1,r2) not in g:
            if r2 <= r1:
                g[(x1,x2,r1,r2)] = 0
                
            else:
                g[(x1,x2,r1,r2)] = x2-x1-1 + min([gold(x1,r[pr]-1,r1,pr)+gold(r[pr],x2,pr+1,r2) for pr in xrange(r1,r2)])

        return g[(x1,x2,r1,r2)]

    p, q = map(int,file.readline().split())
    r = map(int,file.readline().split())

    return gold(0, p, 0, q)
    


file = sys.stdin

case = int(file.readline())

for i in range(case):
    print "Case #" + str(i+1) + ":",
    print compute()
