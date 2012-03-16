% Problem: Old Magician
% Language: BibTeX
% Author: KirarinSnow
% Usage:
%    cat -n input.in |
%      sed -e 's/^ */@case{line/; s/\t/, content = "/; s/$/"}/' >tmp.bib
%    cat -n input.in |
%      sed -e 's/^ */\\citation{line/; s/\t.*/}/' >tmp.aux
%    echo -e "\\\\bibstyle{tmp}\n\\\\bibdata{tmp}" >>tmp.aux
%    cp thisfile.bst tmp.bst
%    bibtex -terse tmp >output.out
% Comments: Requires some preprocessing for input.


ENTRY { content } { } { }
  
INTEGERS { casenumber }
STRINGS { }

FUNCTION {init}
{
  #0 'casenumber :=
}

FUNCTION {case}
{
  casenumber
  {
    "Case #" casenumber int.to.str$ * ": " *
    content duplicate$ text.length$ #1 substring$ chr.to.int$
    { duplicate$ #1 > }
    { #2 - }
    while$
    { "BLACK" } { "WHITE" } if$ * top$
  } { } if$
  casenumber #1 + 'casenumber :=
}

READ
EXECUTE {init}
ITERATE {case}
