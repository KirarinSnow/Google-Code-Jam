#!/usr/bin/python
#
# Problem: Train Timetable
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out

import sys
from math import *

MAX = 1000000000

file = sys.stdin

def train():
    t = int(file.readline())
    na, nb = map(int, file.readline().split())

    trips = []
    for i in range(na+nb):
	tt1, tt2 = file.readline().split()
	t1 = 60*int(tt1[0:2]) + int(tt1[3:5])
	t2 = 60*int(tt2[0:2]) + int(tt2[3:5])
	if i < na:
	    stat = 0
	else:
	    stat = 1

	trips.append([t1,t2,stat])
    trips.sort()

    trains = []
    act = 0
    bct = 0
    for x in trips:
	assigned = 0
	ck = 0
	for iy in range(len(trains)):
	    y = trains[iy]
	    if y[2] != x[2] and x[0] >= y[1] + t:
		trains[iy] = x
		assigned = 1
		break
	if assigned == 0:
	    trains.append(x)
	    if x[2] == 0:
		act += 1
	    else:
		bct +=1
    
    return str(act) + " " + str(bct)


n = int(file.readline())

for i in range(n):
    s = "Case #" + str(i+1) + ": "
    s += train()	
    print s
