# 30: Holman Dynamics (Sales System)
<div align='center'><img src='PB032.gif' /></div>
n
## Instructions
>Create a file in your host containing the contiguous 16-value sequence from the garbage file (file 199) that is a valid credit card number. There will be exactly one such sequence.
>
>For more information see "How to Validate Credit Card Numbers" in the second issue of the zine.

## Solution

### [RD](RD.exa) (GLOBAL)
```asm
LINK 800
LINK 802
LINK 799
GRAB 199
MARK SEEK
COPY 0 X
SEEK -9999
SEEK M
@REP 8
TEST F = -9999
TJMP INVALID
SEEK -1
MULI F 2 T
ADDI X T X
TEST T > 9
FJMP SKIP@{1,1}
SUBI X 9 X
MARK SKIP@{1,1}
TEST F = -9999
TJMP INVALID
SEEK -1
ADDI X F X
@END
MODI X 10 X
TEST X = 0
TJMP FOUND
MARK INVALID
COPY -1 M
JUMP SEEK
MARK FOUND
COPY 200 M
SEEK -9999
SEEK M
@REP 16
COPY F M
@END
```

### [WR](WR.exa) (GLOBAL)
```asm
MAKE
MARK LOOP
COPY X M
TEST M = -1
FJMP FOUND
ADDI X 1 X
JUMP LOOP
MARK FOUND
COPY X M
@REP 16
COPY M F
@END
```