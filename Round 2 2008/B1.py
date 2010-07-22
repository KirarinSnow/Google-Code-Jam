#!/usr/bin/python
#
# Problem: Triangle Areas
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    n, m, a = map(int, raw_input().split())

    if a > n*m:
	return "IMPOSSIBLE"
    else:
	x = (a-1)%n+1
	y = (a-1)/n+1
        return ' '.join(map(str, [0, 1, n, 0, x, y]))


for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
