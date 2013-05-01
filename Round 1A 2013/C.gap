# Problem: Good Luck
# Language: GAP
# Author: KirarinSnow
# Usage: gap -b -q thisfile.gap <input.in >output.out 
# Comments: Breaks on second small for some reason.


stdin := InputTextUser();
total := Int(Chomp(ReadLine(stdin)));


for case in [1 .. total] do;
  Print("Case #", case, ": \n");

  line := SplitString(Chomp(ReadLine(stdin)), " ");
  r := Int(line[1]);
  n := Int(line[2]);
  m := Int(line[3]);
  k := Int(line[4]);

  sets := List(UnorderedTuples([2 .. m], n), i -> [i, NrPermutationsList(i)]);
  d := rec();
  c := rec();

  for index in [1 .. Size(sets)] do;
    set := sets[index];
    pset := List(Tuples([true, false], n), i -> ListBlist(set[1], i));
    g := rec();
    for subset in pset do;
      product := Product(subset);
      if not IsBound(d.(product)) then
        d.(product) := 0;
      fi;
      d.(product) := d.(product) + set[2];
      if not IsBound(g.(product)) then
        g.(product) := 0;
      fi;
      g.(product) := g.(product) + 1; 
    od;
    c.(index) := rec();
    for product in RecNames(g) do;
      c.(index).(product) := g.(product);
    od;
  od;  

  for trial in [1 .. r] do;
    products := List(SplitString(Chomp(ReadLine(stdin)), " "), i -> Int(i));

    maxprob := 0;
    for index in [1 .. Size(sets)] do;
      prob := 1;
      set := sets[index];
      for product in products do;
        if IsBound(c.(index).(product)) then;
          prob := prob * set[2] * c.(index).(product) / d.(product);
        else;
          prob := 0;
        fi;
      od;
      if prob > maxprob then;
        maxprob := prob;
        best := set[1];
      fi;
    od;
    for e in best do;
      Print(e);
    od;
    Print("\n");
  od;
od;

QUIT;
