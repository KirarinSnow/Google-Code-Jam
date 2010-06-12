# Problem: Theme Park
# Language: Octave
# Author: KirarinSnow
# Usage: octave -q thisfile.m <input.in >output.out


# Comments: This was originally going to be a GolfScript solution,
#           since I suppose this theme park offers attractions other
#           than its perennially popular roller coaster. The miniature
#           golf course would be a most appropriate venue to relax in
#           while contemplating the myriad ways in which bytes may be
#           shuffled and programs truncated ("miniature" because this
#           solution wouldn't have stood a chance on the large set...).
#           Alas, as circumstances would have it, my sleep-deprived
#           brain could not conjure up another stack procedure, and
#           thus we have the following Octave solution in its place.
#           Not too exciting as the others, perhaps, but still a pleasant
#           note on which to conclude this qualification round.


input = fscanf(0, "%d", Inf);
c = 2;

for i = 1:input(1)
  printf("Case #%d:", i);
  
  r = input(c);
  k = input(c+1);
  n = input(c+2);
  queue = input((c+3):(c+2+n));
  c = c+3+n;
  
  total = 0;
  index = 0;
  while (r > 0)
      f = 0;
      start = index;
      while (f + queue(index + 1) <= k)
          f += queue(index + 1);
          index = mod(index + 1, n);
          if (index == start)
              break;
          endif
      endwhile
      total += f;
      r -= 1;
  endwhile
  disp(total);
endfor
