// Nand2Tetris Capstone - Part C: Make the Computer Draw a Box
// K = 22
//   Starting row = K = 22
//   Start address = SCREEN + 32*22 = 16384 + 704 = 17088
//   Height = 20 rows
//   Width  = 16 * ((22 mod 4) + 1) = 48 pixels = 3 words per row
// While a key is pressed the box is drawn black; when released it is cleared.

(LOOP)
@KBD
D=M
@BLACK
D;JNE

@WHITE
0;JMP

(BLACK)
@color
M=-1
@DRAW
0;JMP

(WHITE)
@color
M=0

(DRAW)
// addr = SCREEN + 32*22 = 17088
@17088
D=A
@addr
M=D

// rows = 20
@20
D=A
@rows
M=D

(ROW)
@rows
D=M
@LOOP
D;JEQ

// write 3 words (48 pixels) on this row
@color
D=M
@addr
A=M
M=D
A=A+1
M=D
A=A+1
M=D

// addr = addr + 32 (next screen row)
@32
D=A
@addr
M=D+M

@rows
M=M-1

@ROW
0;JMP
