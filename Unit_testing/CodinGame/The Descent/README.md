Theory provided by codingame.com:

In computer programming, standard streams are preconnected input and output communication channels between a computer program and its environment when it begins execution. The three input/output (I/O) connections are called **standard input (stdin)**, **standard output (stdout)** and **standard error (stderr)**.

On CodinGame, the data needed to solve puzzles is given to you in the stdin. Your code needs to print the requested answer in the stdout.

The default code, given in all CodinGame puzzles, already parses the stdin and prints a default output in the stdout.

You can use the stderr for debug purposes. Debug messages will show in the console output (at the bottom left).


You can notice a infinite while loop in the default code. It's the game loop.

Each iteration of the while loop corresponds to a turn of the game where your code must read input data in stdin and output a response in stdout.

The game loop is actually not infinite: there is a max number of turns allowed to solve each puzzle. Once your program sends the expected output or reached the expected state, the referee program (on CodinGame side) will end the loop.

It's really important to continue reading all input data on the stdin each turn; else, your program will desynchronize from the referee program.

With the same idea, if you start reading the input data of turn n+1 on the stdin without having sent a response in the stdout at turn n, the referee program will consider that your program did not respond in due time (timeout).

- Each turn, you must compare the heights of the mountains (given in stdin) to find the highest.
- You should not send in stdout the height of the highest mountain but its index.
- Mountain heights are given in the order of their index. The first height therefore corresponds to the mountain of index 0.

At each game turn:
- Reset to 0 the variables containing the height of the highest mountain and its index
- For each mountain index (from 0 to 7 included):
    - Read the height of the mountain (mountainH variable) on stdin
    - If it's higher than the highest known mountain, save its index and height
- Send the index of the highest mountain on stdout

Pseudo-code
Here's what your code should do at every turn of the game:
max ← 0
imax ← 0
for i starting from 0 to 7 do
	read mountain_h
	if mountain_h is greater than max then
		max ← mountain_h
		imax ← i
	end if

end for
print imax