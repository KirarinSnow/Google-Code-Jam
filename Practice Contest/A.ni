"An Encounter with the Old Magician" by KirarinSnow

[
  Problem: Old Magician
  Language: Inform 7
  Author: KirarinSnow
  Usage:
      cp input.in commands.txt
      echo -e "quit\n\n" >>commands.txt
      rm -r output.scr codejam.inform
      echo -e "s\ncodejam\nq\n" | i7
      cp thisfile.ni codejam.inform/Source/story.ni
      i7 -r codejam
      echo -e "transcript\n\n" | cat - commands.txt |
      frotz -pdq codejam.inform/Build/output.z5
      grep -o "Case.*$" output.scr >output.out
  Comments:
    Needs Inform 7 (http://inform7.com), Frotz (http://frotz.sourceforge.net).
    The above bash commands allow for automatic processing and generate
    an output file (output.out) given an input file (input.in) and the
    current program (thisfile.ni). It creates a new interactive story and
    then runs it using the input file as commands entered by the player. The
    lines containing the solutions for each test case are filtered from the
    session transcript. This story may also be played interactively.
]


The Chamber of Code Jam Awesomeness is a room.

The case count is a number that varies.
The case index is a number that varies.

Processing up to is an action applying to a number.
Computing is an action applying to a topic.

Understand "[a number]" as processing up to.
Understand "[text]" as computing.

Carry out processing up to:
	now the case count is the number understood;
	now the case index is 1.

Carry out computing:
	let S be the number of characters in the topic understood;
	let T be character number S in the topic understood;
	say "Case #[the case index]: [the colour for T]";
	increment the case index;
	let I be the case index;
	let C be the case count;
	if I > C, end the story.

To decide which indexed text is the colour for (T - indexed text):
	change the text of the player's command to T;
	if the player's command matches "[number]":
		let N be the number understood;
		let R be the remainder after dividing N by 2;
		decide on "[if R is even]WHITE[otherwise]BLACK".
