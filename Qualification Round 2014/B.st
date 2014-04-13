"
  Problem: Cookie Clicker Alpha
  Language: Smalltalk
  Author: KirarinSnow
  Usage: gst thisfile.st <input.in >output.out
"


cases := stdin nextLine asNumber.
1 to: cases do: [ :case |
    (case == 1) ifTrue: [stdin nextLine.].
    'Case #' display.
    case display.
    ': ' display.
    line := stdin nextLine tokenize: ' '.
    c := (line at: 1) asNumber.
    f := (line at: 2) asNumber.
    x := (line at: 3) asNumber.
    opt := ((x/c)-(2/f)) ceiling max: 1.
    s := (x-c)/(((opt-1)*f)+2).
    0 to: (opt-1) do: [ :j |
        s := s+(c/(2+(j*f))).
    ].
    s displayNl.
].
