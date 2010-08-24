; Problem: Old Magician
; Language: Arc
; Author: KirarinSnow
; Usage: (cat thisfile.arc - | mzscheme -m -f as.scm | sed '1,3 d')
;          <input.in >output.out
; Comments: http://arclanguage.org/
;           Run in installation directory.


(def main ()
  (prn)
  (quit:for i 1 (read)
    (pr "Case #" i ": ")
    (read)
    (prn:if (is 1 (mod (read) 2)) "BLACK" "WHITE")))

(main)
