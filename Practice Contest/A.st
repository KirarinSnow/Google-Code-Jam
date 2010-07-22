"
  Problem: Old Magician
  Language: Smalltalk
  Author: KirarinSnow
  Usage: gst thisfile.st <input.in >output.out
"


compute := [
    :line |
    bw := (line tokenize: ' ').
    b := (bw at: 2) asNumber.
    (b \\ 2 == 1)
    ifTrue: ['BLACK' displayNl]
    ifFalse: ['WHITE' displayNl].
].

input := stdin lines.
cases := input next asNumber.
i := 0.
input do: [
    :line |
    (i == 0) ifFalse: [
	'Case #' display.
	i display.
	': ' display.
	
	compute value: line.
	].	
    i := i + 1.
].
