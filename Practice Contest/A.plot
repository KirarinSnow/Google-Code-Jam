#!/usr/bin/env gnuplot
#
# Problem: Old Magician
# Language: gnuplot
# Author: KirarinSnow
# Usage: gnuplot thisfile.plot <input.in >output.out


if (!exists("case")) \
  case = 0; \
  ptr = 1; \
  buffer = "`cat /dev/stdin | tr '\n' ' '`"; \
  set print "/dev/stdout"; \
  mode = 0

if (mode == 0) \
  total = word(buffer, ptr); \
  ptr = ptr+1; \
  mode = 1

if (mode == 1) \
  w = int(word(buffer, ptr)); \
  b = int(word(buffer, ptr+1)); \
  ptr = ptr+2; \
  mode = b%2+2

if (mode == 2) \
  ans = "WHITE"; \
  mode = 4

if (mode == 3) \
  ans = "BLACK"; \
  mode = 4

if (mode == 4) \
  case = case+1; \
  print sprintf("Case #%d: %s", case, ans); \
  mode = 1
 
if (case < total) reread
