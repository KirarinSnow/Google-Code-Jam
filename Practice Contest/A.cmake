# Problem: Old Magician
# Language: CMake
# Author: KirarinSnow
# Usage: cp thisfile.cmake CMakeLists.txt && cmake . <input.in 2>output.out
# Comments: Output directed through stderr.


cmake_minimum_required(VERSION 2.8)

file(STRINGS /dev/stdin F)

list(GET F 0 t)

set(p 1)
foreach(i RANGE 1 ${t})
  list(GET F ${p} S)
  math(EXPR p "${p}+1")

  string(REPLACE " " ";" C ${S})
  
  list(GET C 1 b)
  math(EXPR m "${b}%2")
  if(${m} EQUAL 1)
    set(out "BLACK")
  else(${m} EQUAL 1)
    set(out "WHITE")
  endif(${m} EQUAL 1)

  message("Case #" ${i} ": " ${out})
  
endforeach(i)
