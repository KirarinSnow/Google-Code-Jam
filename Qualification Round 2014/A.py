#!/usr/bin/env python
#
# Problem: Magic Trick
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    n1 = int(raw_input())
    b1 = [map(int, raw_input().split()) for i in range(4)]
    n2 = int(raw_input())
    b2 = [map(int, raw_input().split()) for i in range(4)]
    s = set(b1[n1-1]).intersection(set(b2[n2-1]))
    if len(s) == 1:
        ans = list(s)[0]
    elif len(s) > 1:
        ans = "Bad magician!"
    else:
        ans = "Volunteer cheated!"
    print "Case #%d: %s" % (case+1, ans)
