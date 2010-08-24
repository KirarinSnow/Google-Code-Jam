; Problem: Old Magician
; Language: Scheme
; Author: KirarinSnow
; Usage: guile thisfile.scm <input.in >output.out


(use-modules (srfi srfi-1) (ice-9 format))


(define (compute)
  (let ((w (read))
	(b (read)))
    (if (even? b) "WHITE" "BLACK")))

(map
 (lambda (i)
   (format #t "Case #~a: ~a\n" i (compute)))
 (iota (read) 1))
