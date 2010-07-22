(*
 *  Problem: Old Magician
 *  Language: Pascal
 *  Author: KirarinSnow
 *  Usage: gpc thisfile.p -o executable && ./executable <input.in >output.out
 *)


program GCJ;

var
   cases, num : integer;

procedure compute;

var
   W, B : integer;

begin
   read(W);
   read(B);
   if (B mod 2 = 0) then
      write("WHITE")
   else
      write("BLACK");
end;



begin
   read(cases);
   for num := 1 to cases do
   begin
      write("Case #");
      write(num);
      write(": ");
      compute;
      write("\n");
   end;
end.
