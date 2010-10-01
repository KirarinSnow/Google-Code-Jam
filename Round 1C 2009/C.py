#!/usr/bin/python
#
# Problem: Bribe the Prisoners
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    g = dict()

    def gold(x1, x2, r1, r2):
        if (x1, x2, r1, r2) not in g:
            if r2 <= r1:
                g[(x1, x2, r1, r2)] = 0
                
            else:
                m = min([gold(x1, r[pr]-1, r1, pr) + gold(r[pr], x2, pr+1, r2)
                         for pr in xrange(r1, r2)])
                g[(x1, x2, r1, r2)] = x2 - x1 - 1 + m          

        return g[(x1, x2, r1, r2)]

    p, q = map(int, raw_input().split())
    r = map(int, raw_input().split())

    return gold(0, p, 0, q)


for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
