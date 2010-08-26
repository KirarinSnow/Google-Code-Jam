; Problem: Old Magician
; Language: Common Lisp
; Author: KirarinSnow
; Usage: clisp thisfile.lsp <input.in >output.out


(defun compute ()
  (let ((w (read))
	(b (read)))
    (if (= (mod b 2) 0) "WHITE" "BLACK")))

(dotimes (i (read))
  (format t "~&Case #~D: ~A" (1+ i) (compute)))
