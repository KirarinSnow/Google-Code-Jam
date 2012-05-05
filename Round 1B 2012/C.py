#!/usr/bin/env python
#
# Problem: Equal Sums
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Only for small.


for case in range(int(raw_input())):
    s = map(int, raw_input().split())
    n = s.pop(0)
    
    d = {}
    for i in xrange(1<<20):
        z = []
        for j in range(20):
            if (1<<j)&i:
                z.append(s[j])
        t = sum(z)
        if t in d:
            ans = '\n'.join(['']+[' '.join(map(str, x)) for x in [d[t], z]])
            break
        else:
            d[t] = z

    print "Case #%d: %s" % (case+1, ans)
