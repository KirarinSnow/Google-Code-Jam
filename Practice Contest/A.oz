% Problem: Old Magician
% Language: Oz
% Author: KirarinSnow
% Usage: ozc -x thisfile.oz -o exec && ./exec <input.in >output.out


functor
import
   Application
   System
   Open

define
   Stdin = {New class $ from Open.file Open.text end init(name:stdin)}

   Cases = {String.toInt {Stdin getS($)}}
   for X in 1..Cases do
      {System.printInfo "Case #"#X#": "}

      if {IsOdd {String.toInt {String.tokens {Stdin getS($)} & }.2.1}} then
	 {System.showInfo "BLACK"}
      else
	 {System.showInfo "WHITE"}
      end
   end
   
   {Application.exit 0}
end
