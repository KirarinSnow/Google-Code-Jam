#!/usr/bin/env python
#
# Problem: Good Luck
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Should work some reasonable part of the time for the smaller input.


raw_input()
r, n, m, k = map(int, raw_input().split())
print "Case #1: "

for case in range(r):
    z = map(int, raw_input().split())
    q = ['555', '554', '553', '552', '544', '543', '542', '533', '532',
         '444', '443', '442', '433', '432', '333', '332']
    w = map(lambda x: eval('*'.join(list(x))), q)
    for i in range(len(q)):
        if w[i] in z:
            ans = q[i]
            break
    else:
        ans = 522
        
    print ans
