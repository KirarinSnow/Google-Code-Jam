#!/usr/bin/env gnuplot
#
# Problem: Dancing With the Googlers
# Language: gnuplot
# Author: KirarinSnow
# Usage: gnuplot thisfile.plot <input.in >output.out
# Comments: This also writes a PDF plot to "plot.pdf".


if (!exists("case")) \
  case = 0; \
  ptr = 1; \
  buffer = "`cat /dev/stdin | tr '\n' ' '`"; \
  set print "/dev/stdout"; \
  system("echo > plot.dat"); \
  mode = 0

if (mode == 0) \
  total = word(buffer, ptr); \
  ptr = ptr+1; \
  mode = 1

if (mode == 1) \
  n = int(word(buffer, ptr)); \
  s = int(word(buffer, ptr+1)); \
  p = int(word(buffer, ptr+2)); \
  ptr = ptr+3; \
  ans = 0; \
  i = 0; \
  mode = n+2

if (mode == 2) \
  case = case+1; \
  print sprintf("Case #%d: %d", case, ans); \
  system(sprintf("echo %d %d >> plot.dat", case, ans)); \
  mode = 1

if (mode > 2) \
  i = i + 1; \
  z = int(word(buffer, ptr)); \
  ptr = ptr+1; \
  mode = mode-1; \
  b = ((z+2)/3 >= p); \
  c = ((z+2)/3 == p-1 && z%3 != 1 && z > 0 && s > 0); \
  if (b || c) ans = ans+1; \
  if (c) s = s-1
 
if (case < total) reread


# generate plot
set term pdf 
set output 'plot.pdf'
set xlabel 'case'
set ylabel 'answer'
set key off

plot 'plot.dat' using 1:2 with linespoints
