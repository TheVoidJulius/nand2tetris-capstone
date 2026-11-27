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
@17568
D=A
@addr
M=D

@20
D=A
@rows
M=D

(ROW)
@rows
D=M
@LOOP
D;JEQ

@color
D=M
@addr
A=M
M=D
A=A+1
M=D

@32
D=A
@addr
M=D+M

@rows
M=M-1

@ROW
0;JMP