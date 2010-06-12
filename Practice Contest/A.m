# Problem: Old Magician
# Language: Octave
# Author: KirarinSnow
# Usage: octave -q thisfile.m <input.in >output.out


input = fscanf(0,"%d",Inf);

for i = 1:input(1)
  printf("Case #%d: ",i);

  w = {"WHITE", "BLACK"}{1 + mod(input(2*i + 1), 2)};

  disp(w);
endfor
