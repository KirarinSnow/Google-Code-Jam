#!/usr/bin/python
#
# Problem: Mousetrap
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    k = input()
    queries = map(int, raw_input().split())
    n = queries.pop(0)
    
    answers = [None] * n
    
    pos = 0
    for i in xrange(k):
        pos = (pos+i)%(k-i) # next position
        for j in xrange(n):
            if answers[j] == None:
                if queries[j] == pos + 1: # found position
                    answers[j] = i + 1
                elif queries[j] > pos + 1: # shift cards
                    queries[j] -= 1
                        

    return ' '.join(map(str, answers))
    

for i in xrange(input()):
    print "Case #%d: %s" % (i+1, compute())
