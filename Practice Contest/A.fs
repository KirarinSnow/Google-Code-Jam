// Problem: Old Magician
// Language: F#
// Author: KirarinSnow
// Usage: fsharpc thisfile.fs -o exec.exe && ./exec.exe <input.in >output.out
// Comments: http://fsxplat.codeplex.com/


open System

let t = (Int32.Parse (Console.ReadLine ())) in
  for i = 1 to t do
    let b = (Int32.Parse (Seq.nth 1 ((Console.ReadLine ()).Split [|' '|]))) in
      printfn "Case #%d: %s" i (if (b % 2 = 1) then "BLACK" else "WHITE")
