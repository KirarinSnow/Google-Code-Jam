// Problem: Old Magician
// Language: Clean
// Author: KirarinSnow
// Usage: clm -nr thisfile -o executable && ./executable <input.in >output.out
// Comments: http://clean.cs.ru.nl/


module A

import StdEnv

Start :: *World -> *World
Start world
  # (console, world) = stdio world
  # (_, t, console) = freadi console
  # console = foldl compute console [1 .. t]
  # (_, world) = fclose console world
  = world
where 
  compute :: *File Int -> *File
  compute f i
    # f = fwrites ("Case #" +++ fromInt i +++ ": ") f
    # (_, w, f) = freadi f
    # (_, b, f) = freadi f
    # f = fwrites (out b +++ "\n") f
    = f 
  out :: Int -> String
  out b | (b rem 2) == 1 = "BLACK"
  out b = "WHITE"
