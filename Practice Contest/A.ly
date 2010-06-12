% Problem: Old Magician
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out

\version "2.12.1"

#(begin

(define (compute)
    (let ((wb (list (readint) (readint))))
    (if (= (remainder (second wb) 2) 0) "WHITE" "BLACK")))

(define (rint)
  (let* ((c (read-char))
         (s (string c)))
   (if (char-numeric? c)
       (string-append s (rint))
       "")))

(define (readint) (string->number (rint)))


(define n (readint))
(let loop ((i 1))
     (if (<= i n)
	 (begin
	  (display "Case #")
	  (display i)
	  (display ": ")
	  (display (compute))
	  (newline)
	  (loop (+ i 1)))
       'done))
)