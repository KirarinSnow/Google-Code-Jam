(*
 *  Problem: Triangle Areas
 *  Language: Pascal
 *  Author: KirarinSnow
 *  Usage: gpc thisfile.p -o executable
 *         ./executable < input.in > output.out
 *)

program GCJ;

var
   cases, num : integer;

procedure compute;

var
   N, M, A, X, Y : integer;

begin
   read(N);
   read(M);
   read(A);
   if (A > N*M) then
      write("IMPOSSIBLE")
   else
   begin
      write("0 1 ");
      write(N);
      write(" 0 ");
      X := (A-1) mod N + 1;
      Y := (A-1) div N + 1;
      write(X);
      write(" ");
      write(Y);
   end;  
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
