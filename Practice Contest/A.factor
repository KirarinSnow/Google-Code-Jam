! Problem: Old Magician
! Language: Factor
! Author: KirarinSnow
! Usage: factor thisfile.factor <input.in >output.out 


USE: io
USE: kernel
USE: math
USE: math.parser
USE: math.ranges
USE: sequences
USE: splitting


readln string>number [1,b] [
  "Case #" write number>string write ": " write
  readln " " split second string>number odd? [ "BLACK" ] [ "WHITE" ] if print
] each
