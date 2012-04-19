; Problem: Old Magician
; Language: Emacs Lisp
; Author: KirarinSnow
; Usage: emacs -Q --script thisfile.el <input.in >output.out


(dotimes (number (car (read-from-string (read-buffer t))))
  (princ
   (format "Case #%d: %s\n" (1+ number)
	   (let ((b (car (read-from-string
			  (cadr (split-string (read-buffer t)))))))
	     (if (= (if (integerp b) (% b 2)
		      (truncate (* 2 (- (/ b 2) (truncate (/ b 2))))))
		    1)
		 "BLACK" "WHITE")))))
