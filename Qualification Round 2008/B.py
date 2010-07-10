#!/usr/bin/python
#
# Problem: Train Timetable
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out


def compute():
    t = input()
    na, nb = map(int, raw_input().split())

    trips = []
    for i in range(na+nb):
	tt1, tt2 = raw_input().split()
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
    
    return "%d %d" % (act, bct)


for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
