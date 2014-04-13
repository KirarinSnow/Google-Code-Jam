"Don't Play With Fire" by KirarinSnow

[
  Problem: Deceitful War
  Language: Inform 7
  Author: KirarinSnow
  Usage:
      cat input.in | tr '.' '@' > commands.txt
      echo -e "quit\n\n" >>commands.txt
      rm -r output.scr codejam.inform
      echo -e "s\ncodejam\ns\ng\nr\nq\n" | i7
      cp thisfile.ni codejam.inform/Source/story.ni
      i7 -r codejam
      echo -e "transcript\n\n" | cat - commands.txt |
      glulxe codejam.inform/Build/output.ulx
      grep -o "Case.*$" output.scr >output.out
  Comments:
    This works only for the small input. Inform 7 (http://inform7.com) and
    Glulxe (http://www.eblong.com/zarf/glulx) are required to run.
    The above bash commands allow for automatic processing and generate
    an output file (output.out) given an input file (input.in) and the
    current program (thisfile.ni). It creates a new interactive story and
    then runs it using the input file as commands entered by the player. The
    lines containing the solutions for each test case are filtered from the
    session transcript. This story may also be played interactively.
    Note: for some bizarre reason I don't understand, the input gets truncated
    if there are too many instances of '.' on one line. So to get around this,
    all instances of '.' are replaced by '@' before reading in the input.
]


The Gameroom is a room. "This is where Naomi and Ken play War."

The total game count is a number that varies.
The game counter is a number that varies.
The current player is a person that varies.
The block count is a number that varies.
The war score is a number that varies.
The deceitful war score is a number that varies.

Naomi is a person.
Ken is a person.
A person has a number called current score.

The box is a container.
The incinerator is a container.
The balance scale is a container.

A block is a kind of thing. A block has a number called weight.

The box contains 20 blocks.
The incinerator contains lots of flames.

Now Naomi, Ken, the box of blocks, the balance scale, and the incinerator are in the room.


After reading a command:
	if the player's command matches the regular expression "@":
		replace the player's command with "fetch [the player's command]";
	else if the player's command matches "[a number]":
		if the total game count is 0:
			now the total game count is the number understood;
		otherwise:
			increment the game counter;
			now the current player is Naomi;
			replace the player's command with "play a game with [the player's command] blocks each".

Playing a game is an action applying to a number.
Understand "play a game with [number] blocks each" as playing a game.
Carry out playing a game:
	let L be the list of all blocks contained by the incinerator;
	repeat with item running through L:
		unburn item;
	now the block count is the number understood.

Fetching blocks is an action applying to a topic.
Understand "fetch [text]" as fetching blocks.
Carry out fetching blocks:
	let T be the topic understood;
	let N be the block count;
	repeat with x running from 1 to N:
		let K be word number x in T;
		let W be the weight in centigrams for K;
		grab a block of weight W;
	if the current player is Naomi:
		now the current player is Ken;
	otherwise:
		let L be the list of all blocks carried by Naomi;
		add the list of all blocks carried by Ken to L;
		sort L in weight order;
		now the war score is the advantage for Ken with L;
		now the deceitful war score is N minus the advantage for Naomi with L;
		say "Case #[the game counter]: [the deceitful war score] [the war score]";
		let X be the list of all blocks carried by Naomi;
		let Y be the list of all blocks carried by Ken;
		play war with X and Y;
		if the game counter is the total game count:
			end the story.

To decide which number is the weight in centigrams for (K - indexed text):
	replace the regular expression "0@" in K with "";
	replace the regular expression "$" in K with "0000";
	replace the regular expression "(?<=^\d{5}).*$" in K with "";
	let temp be indexed text;
	let temp be the player's command;
	change the text of the player's command to K;
	let P be a number;
	if the player's command matches "[number]":
		let P be the number understood;
	change the text of the player's command to temp;
	decide on P.

To grab a block of weight (W - number):
	let B be a random block in the box;
	now the weight of B is W;
	move B to the current player;
	let J be the weight of B.

To decide which number is the advantage for (P - person) with (L - list of blocks):
	let S be 0;
	let M be 0;
	repeat with item running through L:
		if item is carried by P:
			increment S;
		otherwise:
			decrement S;
		if S is greater than M:
			now M is S;
	decide on M.

To play war with (X - list of blocks) and (Y - list of blocks):
	repeat with player running through {Naomi, Ken}:
		now the current score of the player is 0;
	sort X in weight order;
	sort Y in weight order;
	repeat with N running through X:
		let K be Ken's optimal block in Y for N;
		remove K from Y;
		weigh N and K;
		incinerate N;
		incinerate K;
	say "[line break]Score: [the current score of Naomi] - [the current score of Ken]".

To decide which block is Ken's optimal block in (Y - list of blocks) for (N - block):
	let Q be the number of entries in Y;
	let M be entry Q in Y;
	if the weight of M is less than the weight of N:
		let K be entry 1 in Y;
		remove entry 1 from Y;
		decide on K;
	otherwise:
		let K be entry 1 in Y;
		while the weight of K is less than the weight of N:
			remove entry 1 from Y;
			now K is entry 1 in Y;
		decide on K.

To weigh (N - block) and (K - block):
	move N to the balance scale;
	move K to the balance scale;
	let V be the weight of N;
	let W be the weight of K;
	if V is greater than W:
		increment the current score of Naomi;
	otherwise:
		increment the current score of Ken.
	
To incinerate (B - block):
	move B to the incinerator.

To unburn (B - block):
	move B to the box.

