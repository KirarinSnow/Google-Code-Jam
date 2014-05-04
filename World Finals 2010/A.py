#!/usr/bin/env python
#
# Problem: Letter Stamper
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out
# Comments: Recursion works only with small.


P = ['ABC', 'BCA', 'CAB', 'ACB', 'BAC', 'CBA']
MAX = 1<<32

def best(s, p, n):
    if (s, p, n) not in b:
        if len(s) == 0:  # empty remainder: pop entire stack
            b[(s, p, n)] = n
        else:
            c = s[0]
            ns = s[1:]
            if n == 0:  # empty stack: push until printable, then print
                v = MAX
                for pp in range(6):
                    d = P[pp].find(c)
                    cost = 2+d+best(ns, pp, n+d+1)
                    v = min(v, cost)
                b[(s, p, n)] = v
            else:
                t = P[p][(n-1)%3]
                if c == t:  # top of remainder == top of stack: print
                    b[(s, p, n)] = 1+best(ns, p, n)
                else:
                    v = MAX
                    if c == P[p][n%3]: # next is OK; can push 1
                        v = min(v, 2+best(ns, p, n+1))
                    else: # next is not OK; can push 2
                        v = min(v, 3+best(ns, p, n+2))
                        if n == 1:  # can also switch pattern and push 1
                            v = min(v, 2+best(ns, (p+3)%6, n+1))
                    if n >= 2 and c == P[p][(n-2)%3]:  # can pop 1
                        v = min(v, 2+best(ns, p, n-1))
                    if n >= 3 and c == P[p][n%3]:  # can pop 2
                        v = min(v, 3+best(ns, p, n-2))
                    b[(s, p, n)] = v
    return b[(s, p, n)]

        
for case in range(int(raw_input())):
    s = raw_input()
    b = {}
    ans = min([best(s, p, 0) for p in range(6)])
    print "Case #%d: %s" % (case+1, ans)
