# Problem: Old Magician
# Language: Nimrod
# Author: KirarinSnow
# Usage: nimrod c thisfile.nim && ./thisfile <input.in >output.out 


import strutils

let t = parseInt(readLine(stdin))
for i in countup(1, t):
  let p = parseInt(split(readLine(stdin))[1])
  echo("Case #", i, ": ", ["WHITE", "BLACK"][p mod 2])
