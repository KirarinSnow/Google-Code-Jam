#!/usr/bin/env python
#
# Problem: Dancing With the Googlers
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


for case in range(int(raw_input())):
    t = map(int, raw_input().split())
    n = t.pop(0)
    s = t.pop(0)
    p = t.pop(0)

    ans = len(filter(lambda x: (x+2)/3 >= p, t))
    ans += min(s, len(filter(lambda x: (x+2)/3 == p-1 and x%3 != 1 and x>0, t)))
    
    print "Case #%d: %d" % (case+1, ans)
