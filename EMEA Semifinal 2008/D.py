#!/usr/bin/env python
#
# Problem: Bus Stops
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Fails on large.


def compute():
    def q(s, r):
        if (s, r) in d:
            return d[(s, r)]
        if r == 0:
            if (s >> k) > 0:
                d[(s, r)] = 0
            else:
                d[(s, r)] = 1
        else:
            if (s >> (p-1)) > 0:
                d[(s, r)] = q(((s ^ (1 << (p-1))) << 1) + 1, r-1)
            else:
                d[(s, r)] = 0
                for j in range(p):
                    if (s >> j)%2 > 0:
                        d[(s, r)] += q(((s ^ (1 << j)) << 1) + 1, r-1)
                        d[(s, r)] %= 30031
        return d[(s, r)]

    n, k, p = map(int, raw_input().split())
    d = {}
    c = 0
    s = (1 << k)-1
    return q(s, n-k)

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
