;; Problem: Minimum Scalar Product
;; Language: Scheme
;; Author: KirarinSnow
;; Usage: mzscheme -qr thisfile.scm < input.in > output.out



(require (lib "list.ss") (lib "string.ss") (lib "pregexp.ss"))



;; Compute solution for each case.
(define (compute)
  
  (let ((k (get))
	(a (gets))
	(b (gets)))
    (foldr + 0 (map * (sort a <) (sort b >)))))




;; Split a string.
(define (split str)
  (regexp-split #rx" " str))

;; Convert a string to a number.
(define sn string->number)

;; Convert a string of numbers to a list of numbers.
(define (isplit str)
  (map sn (split str)))

;; Grab a line from input file; convert to number.
(define (get)
  (sn (read-line)))

;; Grab a line from input file; convert to a list of numbers.
(define (gets)
  (isplit (read-line)))


;;;;; Main program.

;; Get # of cases in input set.
(define n (get))

;; Main loop; iterates over all cases.
(let loop ((i 1))
     (if (<= i n)
	 (begin
	  
	  ;; Display case number.
	  (display "Case #")
	  (display i)
	  (display ": ")
	  
	  ;; Compute output and return
	  (display (compute))

	  (newline)

	  ;; Advance to next case.
	  (loop (+ i 1)))
       'done))
