# 23: Xtreme League Baseball (Player Database)
<div align='center'><img src='PB023.gif' /></div>

## Instructions
>The hosts *active* and *penalty* contain files that correspond to extreme baseball players (files 200-299), along with a directory file that contains a list of those files' IDs (file 199). Each player file contains their name and the following statistics in this order: BA, ZA, APB, WRT, OI, OD, PC, and PS.
>
>Create a file in your host with the name of the player with the highest score using EMBER-2's algorithm:
>
>SCORE = (BA + ZA + APB) / 3 + ( WRT \* OI ) / OD + (PC - PS) \* 20
>
>Players in the *penalty* host should be ignored, as they are currently banned from the game.

## Solution

### [RD](RD.exa) (LOCAL)
```asm
LINK 800
MARK LOOP
GRAB M
MODE
SEEK 1
COPY F X
ADDI X F X
ADDI X F X
DIVI X 3 X
COPY F T
MULI T F T
DIVI T F T
ADDI X T X
COPY F T
SUBI T F T
MULI T 20 T
ADDI X T X
COPY X M
TEST M = 50
TJMP HIGHER
MARK NEXTLOOP
DROP
MODE
JUMP LOOP
MARK HIGHER
SEEK -9999
COPY F M
JUMP NEXTLOOP
MARK HALT
```

### [DR](DR.exa) (LOCAL)
```asm
LINK 800
GRAB 199
MARK LOOP
COPY F M
TEST EOF
FJMP LOOP
COPY -1 M
MODE
COPY -9999 M
```

### [WR](WR.exa) (GLOBAL)
```asm
MAKE
COPY -1 F
MARK LOOP
COPY M F
SEEK -1
TEST F = -9999
TJMP HALT
SEEK -1
TEST F > X
TJMP HIGHER
COPY -50 M
SEEK -1
JUMP LOOP
MARK HIGHER
COPY 50 M
SEEK -9999
COPY M F
COPY F X
SEEK -1
JUMP LOOP
MARK HALT
SEEK -1
VOID F

```