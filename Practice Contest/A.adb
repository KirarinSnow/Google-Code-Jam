-- Problem: Old Magician
-- Language: Ada
-- Author: KirarinSnow
-- Usage: gnatmake thisfile.adb && ./thisfile <input.in >output.out


with Ada.Text_IO;
with Ada.Integer_Text_IO;
with Ada.Strings.Fixed;

procedure A is

   T, B, W : Integer := 0;

   procedure Compute is
   begin
      Ada.Integer_Text_IO.Get (W);
      Ada.Integer_Text_IO.Get (B);

      if B mod 2 = 1 then
         Ada.Text_IO.Put_Line ("BLACK");
      else
         Ada.Text_IO.Put_Line ("WHITE");
      end if;

   end Compute;

begin
   Ada.Integer_Text_IO.Get (T);
   for C in 1 .. T loop
      Ada.Text_IO.Put  ("Case #" &
         Ada.Strings.Fixed.Trim (Integer'Image (C), Ada.Strings.Left) & ": ");
      Compute;
   end loop;
end A;
