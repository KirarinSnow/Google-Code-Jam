#!/usr/bin/python
#
# Problem: Get to Work
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 



def compute():
    n,t = map(int, raw_input().split())
    e = input()
    d = [map(int, raw_input().split()) for i in range(e)]

    part = [[]]*n
    
    for i in range(n):
        part[i] = filter(lambda x: x[0] == i+1, d)

    out = [-1]*n
    for i in range(len(part)):
        if part[i] == []:
            out[i] = 0
        elif i+1 == t:
            out[i] = 0
        else:
            cars = [ x[1] for x in part[i] ]
            cars.sort()
            cars = cars[::-1]
            need = len(cars)
            count = 0
            j = 0
            while need > 0 and j < len(cars):
                count += 1
                need -= cars[j]
                j += 1
            if need > 0:
                return "IMPOSSIBLE"
            else:
                out[i] = count
    
    return ' '.join(map(str, out))


for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())

