# Problem: Candy Splitting
# Language: CMake
# Author: KirarinSnow
# Usage: cp thisfile.cmake CMakeLists.txt && cmake . <input.in 2>output.out
# Comments: Output directed through stderr.


cmake_minimum_required(VERSION 2.8)

file(STRINGS /dev/stdin F)

list(GET F 0 t)

set(p 1)
foreach(i RANGE 1 ${t})
  list(GET F ${p} n)
  math(EXPR p "${p}+1")
  list(GET F ${p} S)
  math(EXPR p "${p}+1")

  string(REPLACE " " ";" C ${S})
  
  set(patrick 0)
  set(sean 0)
  set(min 1000000)
  foreach(j ${C})
    math(EXPR patrick "${patrick}^${j}")
    math(EXPR sean "${sean}+${j}")
    if(${j} LESS ${min})
      set(min ${j})
    endif(${j} LESS ${min})
  endforeach(j)

  set(out "NO")
  if(${patrick} EQUAL 0)
    math(EXPR out "${sean}-${min}")
  endif(${patrick} EQUAL 0)
  message("Case #" ${i} ": " ${out})
  
endforeach(i)
