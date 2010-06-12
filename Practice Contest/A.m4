dnl  Problem: Old Magician
dnl  Language: m4
dnl  Author: KirarinSnow
dnl  Usage: m4 thisfile.m4 <input.in >output.out
dnl
define(I, 0)dnl
divert(-1)dnl
patsubst(
  include(/dev/stdin),
    `^.* \(.*\)', 
    `divert`'define(`I',incr(I))Case `#'I: ifelse(eval(\1%2),0,WHITE,BLACK)')