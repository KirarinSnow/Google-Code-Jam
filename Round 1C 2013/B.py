#!/usr/bin/env python
#
# Problem: Pogo
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Small only.


for case in range(int(raw_input())):
    x, y = map(int, raw_input().split())

    s = ["EW", "WE"][x>0]*abs(x) + ["NS", "SN"][y>0]*abs(y)

    print "Case #%d: %s" % (case+1, s)
