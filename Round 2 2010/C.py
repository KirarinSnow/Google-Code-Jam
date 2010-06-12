#!/usr/bin/python
#
# Problem: Bacteria
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 
# Comments: Times out on large set.



MAX = 101

def compute():
    table = []
    for i in range(MAX):
        table.append([0]*MAX)

    count = 0

    r = input()
    for i in range(r):
        l = map(int, raw_input().split())
        for x in range(l[0], l[2]+1):
            for y in range(l[1], l[3]+1):
                if table[x][y] == 0:
                    table[x][y] = 1
                    count += 1

    steps = 0
    while count > 0:
        steps += 1
        for x in range(MAX)[::-1]:
            for y in range(MAX)[::-1]:
                try:
                    if table[x][y] == 0 and table[x-1][y] == 1 and table[x][y-1] == 1:
                        table[x][y] = 1
                        count += 1
                    if table[x][y] == 1 and table[x-1][y] == 0 and table[x][y-1] == 0:
                        table[x][y] = 0
                        count -= 1
                except:
                    pass
    
    return steps
    

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
