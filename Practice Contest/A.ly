% Problem: Old Magician
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out


\version "2.12.1"


#(define (compute)
  (let ((wb (list (read) (read))))
   (if (= (remainder (second wb) 2) 0) "WHITE" "BLACK")))

#(map
  (lambda (i)
   (format #t "Case #~a: ~a\n" i (compute)))
  (iota (read) 1)))
