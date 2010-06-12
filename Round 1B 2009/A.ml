(*
 *  Problem: Decision Tree
 *  Language: OCaml
 *  Author: KirarinSnow
 *  Usage: ocaml thisfile.ml <input.in >output.out
 *)

#load "str.cma";;

let tree () =
  
  (* Read tree *)
  let t =
    let nd = read_int () in
    let rec readdt dt j =
      if j > nd then dt else
	readdt (dt @ [read_line ()]) (j+1) in
      Str.global_replace (Str.regexp " ") "" (Str.global_replace (Str.regexp "\\b") "^" (String.concat "" (readdt [] 1))) in
    
  (* Read feature list *)
  let na = read_int () in
  let rec readan k =
    if k > na then () else
      let an = List.tl (List.tl 
			  (Str.split (Str.regexp " ") (read_line ()))) in

      (* Parse and compute *)
      let rec parse s l p = 
	if l = 0 then
	  let o = String.index s '(' in
	  let c = String.index s ')' in
	  let f = String.sub s (o+1) (c-o-1) in
	    if String.contains f '(' then
	      let m = String.index s '^' in
	      let w = String.index_from s (m+1) '^' in 
		if List.mem (String.sub s (m+1) (w-m-1)) an then
		  parse (String.sub s (w+1) (String.length s - w - 1))
		      0 (p *. (float_of_string (String.sub s (o+1) (m-o-1))))
		else
		  parse (String.sub s (w+1) (String.length s - w - 1))
		      (-1) (p *. (float_of_string (String.sub s (o+1) (m-o-1))))
	    else p *. (float_of_string f)
	else
	  let o = String.index s '(' in
	  let c = String.index s ')' in
	    if o < c then
	      parse (String.sub s (o+1) (String.length s - o - 1))
		  (if l = -1 then 1 else l+1) p
	    else
	      parse (String.sub s (c+1) (String.length s - c - 1))
		  (l-1) p in
	
	print_float (parse t 0 1.0);
	print_newline ();
	
	readan (k+1) in
    readan 1;;

(* Case loop *)
for i = 1 to read_int () do
  Printf.printf "Case #%d:\n" i;
  tree ();
done;;
