(*
 *  Problem: Old Magician
 *  Language: OCaml
 *  Author: KirarinSnow
 *  Usage: ocaml thisfile.ml <input.in >output.out
 *)


open Scanf;;
open Printf;;

let cases = read_int ();;

let compute () =
    scanf "%d %d\n" (fun x y -> if y mod 2 = 0 then "WHITE" else "BLACK");;

let rec loop i =
    if i > cases
    then ()
    else begin printf "Case #%d: %s\n" i (compute ()); loop(i+1) end;;

loop 1;;
