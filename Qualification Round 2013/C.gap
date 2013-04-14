# Problem: Fair and Square
# Language: GAP
# Author: KirarinSnow
# Usage: gap -b -q thisfile.gap <input.in >output.out 


stdin := InputTextUser();
total := Int(Chomp(ReadLine(stdin)));

ps := [1, 2, 3];
for x in [0 .. 48] do;
  Add(ps, 2*10^(x+1)+2);
od;
for x in [0 .. 23] do;
  Add(ps, (2*10^(x+1)+1)*10^(x+1)+2);
od;

for i in [0 .. 23] do;
  for j in [0 .. 1] do;
    for k in Combinations([0 .. i-1], j) do;
      t := 10^i;
      for v in k do;
        t := t + 10^v;
      od;
      l := String(t);
      r := Reversed(l);
      Add(ps, Int(Concatenation(l, "2", r)));
    od;
  od;
od;

for i in [0 .. 24] do;
  for j in [0 .. 3] do;
    for k in Combinations([0 .. i-1], j) do;
      t := 10^i;
      for v in k do;
        t := t + 10^v;
      od;
      l := String(t);
      r := Reversed(l);
      Add(ps, Int(Concatenation(l, r)));
      if i < 24 then
        Add(ps, Int(Concatenation(l, "1", r)));
	Add(ps, Int(Concatenation(l, "0", r)));
      fi; 
    od;
  od;
od;

Sort(ps);

search := function(x)
  local l, u, m;
  l := 0;
  u := Size(ps);
  while u > l+1 do;
    m := QuoInt(u+l, 2);
    if x < ps[m+1]*ps[m+1] then
      u := m;
    else
      l := m;
    fi;
  od;
  return l;
end;

for i in [1 .. total] do;
  line := SplitString(Chomp(ReadLine(stdin)), " ");
  a := Int(line[1]);
  b := Int(line[2]);

  x := search(a);
  y := search(b);

  c := y-x;
  if a = ps[x+1]*ps[x+1] then
    c := c + 1;
  fi;
  
  Print("Case #", i, ": ", c, "\n");
od;

QUIT;
