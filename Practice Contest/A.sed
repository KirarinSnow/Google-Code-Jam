#!/bin/sed
#
# Problem: Old Magician
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed <input.in >output.out



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
s/[0-9 ]*[02468]$/WHITE/;
s/[0-9 ]*[13579]$/BLACK/;


# Write case number
s/^/Case \#/;
G;
s/\n/:/;
s/Y//;
s/#\(.*\):\(.*\)/#\2: \1/;
