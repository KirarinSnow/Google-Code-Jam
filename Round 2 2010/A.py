#!/usr/bin/python
#
# Problem: Elegant Diamond
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Might take a while. Try using pypy for faster results.

     
for case in range(int(raw_input())):
    k = int(raw_input())
    s = 2*k-1
    g = map(lambda x: x+(s-len(x))*' ', [raw_input() for i in range(s)])

    m = 1<<32
    for i in range(s):
        for j in range(s):
            f = True
            for x in range(s):
                for y in range(s):
                    if g[x][y] != ' ':
                        xx = 2*i-x
                        yy = 2*j-y
                        
                        if 0 <= xx < s and g[xx][y] not in (' ', g[x][y]):
                                f = False
                        if 0 <= yy < s and g[x][yy] not in (' ', g[x][y]):
                                f = False
            if f:
                m = min(m, abs(i-k+1)+abs(j-k+1))
        
    ans = (m+k)**2-k**2
    print "Case #%d: %d" % (case+1, ans)
