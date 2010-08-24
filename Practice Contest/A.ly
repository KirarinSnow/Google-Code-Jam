% Problem: Old Magician
% Language: LilyPond
% Author: KirarinSnow
% Usage: lilypond thisfile.ly <input.in >output.out


\version "2.12.1"


#(define (compute)
  (let ((w (read))
	(b (read)))
   (if (even? b) "WHITE" "BLACK")))

#(map
  (lambda (i)
   (format #t "Case #~a: ~a\n" i (compute)))
  (iota (read) 1))
