#!/bin/sed
#
# Problem: Alien Language
# Language: sed
# Author: KirarinSnow
# Usage: sed -f thisfile.sed <input.in >output.out
# Comments: Works only on small input.


# Initialize case counter; store words to hold space
1 {
  s/\(.*\) \(.*\) \(.*\)/V0YX\2B/
  s/2\(.\)B/bb\1B/
  s/1\(.\)B/b\1B/
  s/b/aaaaaaaaaa/g
  s/9B/aaaaaaaaaB/
  s/8B/aaaaaaaaB/
  s/7B/aaaaaaaB/
  s/6B/aaaaaaB/
  s/5B/aaaaaB/
  s/4B/aaaaB/
  s/3B/aaaB/
  s/2B/aaB/
  s/1B/aB/
  s/0B/B/

  :word;
  
  /a\(.*\)B/ {
    N
    s/a//
    s/\n/,/
    b word
  }

  s/$/W/
  h
  d
}


# Case counter increment
x
s/9999Y/Y0000X/
s/99Y/Y00X/
s/9Y/Y0X/
s/8Y\(.*\)X/9\1ZX/
s/7Y\(.*\)X/8\1ZX/
s/6Y\(.*\)X/7\1ZX/
s/5Y\(.*\)X/6\1ZX/
s/4Y\(.*\)X/5\1ZX/
s/3Y\(.*\)X/4\1ZX/
s/2Y\(.*\)X/3\1ZX/
s/1Y\(.*\)X/2\1ZX/
s/0\?Y\(.*\)X/1\1ZX/
s/Z/Y/
x


# Solve

G
s/\(.*\)\n\(.*\)/\2\1/
s/V.*B//

# Parenthesize single tokens
:sp
s/W\([a-z]\)/W(\1)/
s/)\([a-z]\)/)(\1)/
t sp


# Check match
s/$/Q/
s/W/WT/
s/,/P,/

:check
s/P,/,P/
t check
/P\([a-z]\).*T([a-z]*\1[a-z]*)/ {
  s/P\([a-z]\)\(.*\)T\(([a-z]*)\)/\1P\2\3T/
  s/W\(.*\)TQ/WT\1QR/
}
t check

/PW/ {
  s/^.*Q//
  s/$/0YX/ 
  b count
}
s/,\([a-z]*\)P\([a-z]*\)/,\1\2P/
s/W\(.*\)T/WT\1/
b check

# Count successes
:count
/^R/ { 
  s/R//
  s/99Y/Y00X/
  s/9Y/Y0X/
  s/8Y\(.*\)X/9\1ZX/
  s/7Y\(.*\)X/8\1ZX/
  s/6Y\(.*\)X/7\1ZX/
  s/5Y\(.*\)X/6\1ZX/
  s/4Y\(.*\)X/5\1ZX/
  s/3Y\(.*\)X/4\1ZX/
  s/2Y\(.*\)X/3\1ZX/
  s/1Y\(.*\)X/2\1ZX/
  s/0\?Y\(.*\)X/1\1ZX/
  s/Z/Y/
}
t count
s/[YX]//g


# Write case number
s/^/Case \#/
G
s/\n/:/
s/Y//
s/V//
s/X.*W//
s/#\(.*\):\(.*\)/#\2: \1/
