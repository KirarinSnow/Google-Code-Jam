#!/bin/sed
#
# Problem: Snapper Chain
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed <input.in >output.out


# Initialize case counter to 0 and store to hold space.
# Include digits for incrementing the case counter.
1 s/.*/0<>0123456789/
1 h
1 d

# Include digits for decrementing N.
s/^/9876543210,/
s/ /< /

# Loop: Decrement number (decr subloop handles numbers ending in 0).
:loop
:decr
s/0</<9/
t decr
s/\(\(.\)\(.\).*,.*\)\2<\(.*\) /\1\3\4< /

# If 0, we are done; since the process finished, it is a success.
#   Bypass the part that adds 'OFF', so the answer will be 'ON'.
/,</b finish

# Division by 2. Make one pass through the number from the left,
#   operating on two digits at a time. The first digit is a temporary
#   digit holding the modulus (by 2) of the previous division.

# Let the first temp digit be 0.
s/ / >0/

# Division loop: In each iteration, move forward as far as possible.
:divide
s/>19/9>1/
s/>18/9>0/
s/>17/8>1/
s/>16/8>0/
s/>15/7>1/
s/>14/7>0/
s/>13/6>1/
s/>12/6>0/
s/>11/5>1/
s/>10/5>0/
s/>09/4>1/
s/>08/4>0/
s/>07/3>1/
s/>06/3>0/
s/>05/2>1/
s/>04/2>0/
s/>03/1>1/
s/>02/1>0/
s/>01/0>1/
s/>00/0>0/
t divide

# If it is impossible to move any further, we have reached the end of
#   the division process. If the temp digit is 1, then we simply remove it
#   to clean up the space. If this occurs, then the loop is repeated.
# Otherwise, execution passes to the next line.
s/>1$//
t loop

# If execution gets here, then there was a 0 bit somewhere in the last
#   n bits of k. Therefore, the answer should be OFF.
s/$/OFF/

# Finish: Remove everything before the 'O' in 'OFF', if there is one.
# Otherwise, there should be a space still in the pattern space, so
#   change everything to 'ON'.
:finish
s/.*O/O/
s/.* .*/ON/

# Swap spaces and increment case number, then reswap.
x
:caseincr
s/9</<0/
t caseincr
s/^</0</
s/\(.\?\)<\(.*\)\(>.*\1\(.\)\)/\4\2<\3/
x

# Copy case number from hold space and reorganize into output format.
G
s/\(.*\)\n\(.*\)<.*/Case #\2: \1/
