#!/bin/sed -f
#
# Problem: Magicka
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed <input.in >output.out



# Initialize case counter to 0 and store to hold space.
# Include digits for incrementing the case counter.
1 s/.*/0<>0123456789/
1 h
1 d


# Remove numbers.
s/[0-9]//g

# Initialize pointer in string.
s/\(\w\+\)$/ >&/


# Loop: invoke all elements after the first.
: invoke

# Apply combination rule.
s/\( \(\w\)\(\w\)\(\w\) .*\)\2>\3/\1\4</
s/\( \(\w\)\(\w\)\(\w\) .*\)\3>\2/\1\4</

# Apply opposition rule.
s/\( \(\w\)\(\w\) .* \)\(\w*\2\w*\)>\3/\1</
s/\( \(\w\)\(\w\) .* \)\(\w*\3\w*\)>\2/\1</

# Apply default rule.
s/>\(.\)/\1</

# Prepare for next application.
s/<\b/>/
t invoke


# Format for output.
s/.* /[/
s/\w\B/&, /g
s/<$/]/


# Swap spaces and increment case number, then reswap.
x
: caseincr
s/9</<0/
t caseincr
s/^</0</
s/\(.\?\)<\(.*\)\(>.*\1\(.\)\)/\4\2<\3/
x

# Copy case number from hold space and reorganize into output format.
G
s/\(.*\)\n\(.*\)<.*/Case #\2: \1/
