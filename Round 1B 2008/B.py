#!/usr/bin/python
#
# Problem: Number Sets
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


from math import *


MAX = 1000000
prime = [True]*(MAX+1)
for n in xrange(2,int(sqrt(MAX))+1):
    for i in xrange(2*n, MAX+1, n):
        prime[i] = False

parent = [0]*(MAX+1)
size = [0]*(MAX+1)


def compute():
    a, b, p = map(int, raw_input().split())
    
    # reset pointers
    for i in xrange(b-a+1):
        parent[i] = i
        size[i] = 1

    count = b-a+1

    # iterate over primes
    n = p
    while n <= min(b, MAX):
        if prime[n]:
            f = (n - a%n)%n # first multiple of prime in interval

            for g in xrange(f+n, b-a+1, n): # iterate over multiples
                
                # find head of tree containing g
                head = g
                while parent[head] != head:
                    head = parent[head]
                
                # update main tree's head
                while parent[f] != f:
                    f = parent[f]

                if f != head: # not in same tree; merge
                    count -= 1
                    if size[f] < size[head]: # merge f into head
                        parent[f] = head
                        size[head] += size[f]
                    else: # merge head into f
                        parent[head] = f
                        size[f] += size[head]

        n += 1
            
    return count
 

for i in range(input()):
    print "Case #%d: %d" % (i+1, compute())
