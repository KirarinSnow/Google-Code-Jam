#!/usr/bin/python
#
# Problem: Picking Up Chicks
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    n, k, b, t = map(int, raw_input().split())
    x = map(int, raw_input().split())
    v = map(int, raw_input().split())

    final = map(lambda i: x[i]+v[i]*t, range(n))
    
    count = 0
    arrivals = 0
    pos = n-1
    while arrivals < k and pos >= 0:
        if final[pos] >= b:
            pos -= 1
            arrivals += 1
        else:
            p2 = pos-1
            c2 = 1
            while p2 >= 0 and final[p2] < b:
                p2 -= 1
                c2 += 1
            if p2 < 0:
                return "IMPOSSIBLE"
            count += c2
            temp = final[p2]
            final[p2] = final[pos]
            final[pos] = temp

    return count

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
