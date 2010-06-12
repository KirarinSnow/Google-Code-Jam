#!/bin/sed
#
# Problem: The Next Number
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed < input.in > output.out



# Initialize case counter; delete first line
1 {s/.*/0Y/; h; d;};

# Case counter increment
x;
s/9999Y/Y0000/;
s/99Y/Y00/;
s/9Y/Y0/;
s/8Y\(.*\)$/9\1Z/;
s/7Y\(.*\)$/8\1Z/;
s/6Y\(.*\)$/7\1Z/;
s/5Y\(.*\)$/6\1Z/;
s/4Y\(.*\)$/5\1Z/;
s/3Y\(.*\)$/4\1Z/;
s/2Y\(.*\)$/3\1Z/;
s/1Y\(.*\)$/2\1Z/;
s/0\?Y\(.*\)$/1\1Z/;
s/Z/Y/;
x;


# Solve
s/$/S/;
s/^/0/;

# Find largest decreasing suffix
:suffix;
s/\([0-9]\)0S/\1S0/;
s/\([1-9]\)1S/\1S1/;
s/\([2-9]\)2S/\1S2/;
s/\([3-9]\)3S/\1S3/;
s/\([4-9]\)4S/\1S4/;
s/\([5-9]\)5S/\1S5/;
s/\([6-9]\)6S/\1S6/;
s/\([7-9]\)7S/\1S7/;
s/\([8-9]\)8S/\1S8/;
s/99S/9S9/;
tsuffix;

s/\([0-9]\)S/S\1/;

s/\([0-9]\)S\(.*\)$/\1S\2\1/;

# Bubble sort suffix with copy of preceding digit
s/S/ST/;
:sort;
s/T\([0-9]\)/\1T/;
s/\([1-9]\)T0/0T\1/;
s/\([2-9]\)T1/1T\1/;
s/\([3-9]\)T2/2T\1/;
s/\([4-9]\)T3/3T\1/;
s/\([5-9]\)T4/4T\1/;
s/\([6-9]\)T5/5T\1/;
s/\([7-9]\)T6/6T\1/;
s/\([8-9]\)T7/7T\1/;
s/\([9-9]\)T8/8T\1/;
tsort;

# Verify increasing monotonicity
:verify;
s/\([0-9]\)9T/\1T9/;
s/\([0-8]\)8T/\1T8/;
s/\([0-7]\)7T/\1T7/;
s/\([0-6]\)6T/\1T6/;
s/\([0-5]\)5T/\1T5/;
s/\([0-4]\)4T/\1T4/;
s/\([0-3]\)3T/\1T3/;
s/\([0-2]\)2T/\1T2/;
s/\([0-1]\)1T/\1T1/;
s/00T/0T0/;
tverify;

s/\([0-9]\)T/T\1/;

/S\([0-9]\+\)T/ {
    s/S\([0-9]\+\)T/ST\1/;
    bsort;
};

# At this point, suffix with copy of preceding digit has been sorted.

# Swap preceding digit with next higher digit in suffix

s/8ST\([0-8]*\)\([9-9]\)/\2ST\1/;
s/7ST\([0-7]*\)\([8-9]\)/\2ST\1/;
s/6ST\([0-6]*\)\([7-9]\)/\2ST\1/;
s/5ST\([0-5]*\)\([6-9]\)/\2ST\1/;
s/4ST\([0-4]*\)\([5-9]\)/\2ST\1/;
s/3ST\([0-3]*\)\([4-9]\)/\2ST\1/;
s/2ST\([0-2]*\)\([3-9]\)/\2ST\1/;
s/1ST\([0-1]*\)\([2-9]\)/\2ST\1/;
s/0ST\([0-0]*\)\([1-9]\)/\2ST\1/;


# Clean up
s/ST//;
s/^0//;


# Write case number
s/^/Case \#/;
G;
s/\n/:/;
s/Y//;
s/#\(.*\):\(.*\)/#\2: \1/;
