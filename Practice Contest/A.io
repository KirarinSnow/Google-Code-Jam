# Problem: Old Magician
# Language: Io
# Author: KirarinSnow
# Usage: io thisfile.io <input.in >output.out 


for (i, 1, File standardInput readLine asNumber,
  b := File standardInput readLine split at(1) asNumber
  if (b % 2 == 1) then (out := "BLACK") else (out := "WHITE")
  "Case \##{i}: #{out}" interpolate println
)
