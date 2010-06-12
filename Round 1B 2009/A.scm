;; Problem: Decision Tree
;; Language: Scheme
;; Author: KirarinSnow
;; Usage: mzscheme -qr thisfile.scm < input.in > output.out



(require (lib "list.ss") (lib "string.ss") (lib "pregexp.ss"))




;; Compute solution for each case.
(define (compute)
  
  (let* ((l (get))
	 (dtl (let loop ((i 1)
			 (s "\'"))
		(if (> i l)
		    s
		    (loop (+ i 1) (string-append s (read-line))))))

	 (a (get))
	 
	 (desc (let lp ((i 1)
			(s "\'("))
		 (if (> i a)
		     (string-append s ")")
		     (lp (+ i 1) (string-append s 
						"(" (read-line) ")")))))
	 (dt (eval (read-from-string dtl)))
	 (da (eval (read-from-string desc))))
    
    ;; loop through animals
    (let loop ((r da))
      (if (null? r)
	  'done
	  (begin
	    (let* ((animal (car r))
		   (feat (cddr animal)))
	      
	      (newline)
	      (display

	       (real->decimal-string 
		
		(let lp ((d dt)
			 (p 1))
		  (if (null? (cdr d))
		      (* p (car d))
		      
		      (if (member (cadr d) feat)
			  
			  (lp (caddr d) (* p (car d)))
			  (lp (cadddr d) (* p (car d))))
		      ))
		
		7)
	       
	      ))
	    (loop (cdr r)))))))




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
	  
	  ;; Compute output 
	  (compute)

	  (newline)

	  ;; Advance to next case.
	  (loop (+ i 1)))
       'done))
