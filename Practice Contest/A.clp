; Problem: Old Magician
; Language: CLIPS
; Author: KirarinSnow
; Usage: (cat thisfile.clp - | clips | sed '/CLIPS/d') <input.in >output.out


(deffunction main ()
  (printout t crlf)
  (loop-for-count (?case 1 (read)) do
    (printout t
      "Case #" ?case ": "
      (if (eq 1 (mod (nth 2 (str-explode (readline))) 2))
        then "BLACK"
        else "WHITE")
      crlf))
  (exit))

(main)
