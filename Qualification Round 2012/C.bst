% Problem: Recycled Numbers
% Language: BibTeX
% Author: KirarinSnow
% Usage:
%   echo "@preamble{ \"" >tmp.bib
%   cat input.in >>tmp.bib
%   echo -e "\" }\\n@null{null}\\n" >>tmp.bib
%   echo -e "\\\\citation{null}\n\\\\bibstyle{tmp}\n\\\\bibdata{tmp}" >tmp.aux
%   cp thisfile.bst tmp.bst
%   bibtex -terse tmp >output.out
% Comments: Requires some preprocessing for input. Only for small input.



% when life gives you numbers ... make a bibliography

ENTRY { content } { } { }
  
INTEGERS { cases casenumber a b c l s x first second }
STRINGS { buffer int y }


FUNCTION {null} { }

FUNCTION {and}
{
  'skip$ {pop$ #0} if$
}

FUNCTION {not}
{
  {#0} {#1} if$
}

FUNCTION {mul}
{
  'first := 'second :=
  #0 {second #0 >} {first + second #1 - 'second :=} while$
}

FUNCTION {str.to.int}
{
  #0 swap$
  {duplicate$ empty$ not}
  {swap$ #10 mul 'first :=
   duplicate$ #1 #1 substring$ chr.to.int$ #48 - first + swap$
   duplicate$ text.length$ #1 - #2 swap$ substring$} while$ pop$   
}


FUNCTION {readint}
{
  "" 'int :=
  {
    #1 buffer #1 #1 substring$ " " = -
  }
  {
    buffer #1 #1 substring$ int swap$ * 'int :=
    buffer duplicate$ text.length$ #1 - #2 swap$ substring$ 'buffer :=
  } while$
  buffer duplicate$ text.length$ #1 - #2 swap$ substring$ 'buffer :=
  int str.to.int
}


FUNCTION {jam}
{
  #0 'casenumber :=

  preamble$ duplicate$ text.length$ #1 - #2 swap$ substring$ 'buffer :=
  readint 'cases :=
  {
    casenumber cases <
  }
  {
    casenumber #1 + 'casenumber :=
    
    readint 'a :=
    readint 'b :=
    int text.length$ 'l :=
    
    #0 'c :=
    a 'x :=
    {
      x b #1 + <
    }
    {
      x int.to.str$ 'y :=
      y duplicate$ #1 #1 substring$
      swap$ duplicate$ text.length$ #1 - #2 swap$ substring$
      swap$ * 'y :=      

      #1 's :=
      {
	s l < x y str.to.int = not and
      }
      {
	x y str.to.int < y str.to.int b #1 + < and
	{
	  c #1 + 'c :=
	} { } if$
	
	y duplicate$ #1 #1 substring$
	swap$ duplicate$ text.length$ #1 - #2 swap$ substring$
	swap$ * 'y :=
	s #1 + 's :=
      } while$
      
      x #1 + 'x :=
    } while$
   
    
    "Case #" casenumber int.to.str$ * ": " * c int.to.str$ * top$
  } while$
}

READ

EXECUTE {jam}
