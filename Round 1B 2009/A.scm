;; Problem: Decision Tree
;; Language: Scheme
;; Author: KirarinSnow
;; Usage: guile thisfile.scm <input.in >output.out


(use-modules (srfi srfi-1) (ice-9 format))

(letrec
    ((mapover
      (lambda (a) (map a (iota (read) 1))))
     
     (prob
      (lambda (f q)
	(* (car q)
	   (if (any list? q)
	       (prob f ((if (memq (cadr q) f) caddr cadddr) q)) 1)))))
  
  (mapover
   (lambda (i) (read) (set! @(read))
	   (format #t "Case #~a:~%~{~,7f~%~}" i
		   (mapover
		    (lambda i (read) (prob
				      (mapover (lambda i (read))) @)))))))
