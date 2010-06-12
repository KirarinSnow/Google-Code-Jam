#!/usr/bin/python
#
# Problem: Theme Park
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    r, k, n = map(int, raw_input().split())
    queue = map(int, raw_input().split())
    seen = [False]*n

    total = 0
    index = 0
    rides = 0
    rc = [0]*n

    while (not seen[index]) and (rides < r):
        seen[index] = True
        f = 0
        start = index
        while (f+queue[index] <= k):
            f+=queue[index]
            index= (index+1)%n
            if index == start:
                break
        total += f
        rc[rides] = f
        rides += 1


    if rides < r:
        seen = [False]*n
        rpc = 0
        cost = 0
        while not seen[index]:
            seen[index] = True
            f = 0
            start = index
            while (f+queue[index] <= k):
                f+=queue[index]
                index= (index+1)%n
                if index == start:
                    break
            rpc += 1
            cost += f

        reps = ((r-rides)/rpc)
        total += cost*reps
        rides += rpc*reps
        while rides < r:
            f = 0
            start = index
            while (f+queue[index] <= k):
                f+=queue[index]
                index= (index+1)%n
                if index == start:
                    break
            total += f
            rides += 1
        
    return total
    

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
