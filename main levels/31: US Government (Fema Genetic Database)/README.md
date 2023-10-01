# 31: US Government (Fema Genetic Database)
<div align='center'><img src='PB033.gif' /></div>

## Instructions
>﻿Overwrite the genetic sequence of ‗SEN WALKER CAINE JR‗ with the genetic sequence of ‗PRES WALKER CAINE‗ so that it looks like the younger politician is actually a clone of the older politician.
>
>The names of these two politicians are available in file 300.
>
>Note that you may need to overwrite a data chunk with another data chunk from the same file.
>
>For more information see "Accessing Data in Legacy Storage Systems" in the first issue of the zine.

## Solution

### [DR](DR.exa) (GLOBAL)
```asm
LINK 800
LINK 801
GRAB 200
COPY M X
MARK SEEKPRES
TEST F = X
FJMP SEEKPRES
MARK PRESLOOP
COPY F M
TEST EOF
TJMP NEXT
TEST F > 0
FJMP NEXT
SEEK -1
JUMP PRESLOOP

MARK NEXT
COPY -1 M
COPY M X
SEEK -9999
MARK SEEKSEN
TEST F = X
FJMP SEEKSEN
MARK SENLOOP
COPY F M
TEST EOF
TJMP END
TEST F > 0
FJMP END
SEEK -1
JUMP SENLOOP

MARK END
COPY -1 M
```

### [WR](WR.exa) (GLOBAL)
```asm
GRAB 300
LINK 800
LINK 801
COPY F M
MODE
LINK -1
DROP
MAKE
LINK 801
MARK PRESLOOP
MODE
COPY M X
TEST X = -1
TJMP NEXT
MODE
REPL PRESRUN
@REP 10
COPY M F
@END
JUMP PRESLOOP

MARK NEXT
DROP
LINK -1
GRAB 300
SEEK 1
COPY F X
WIPE
LINK 801
COPY X M
GRAB 400
MODE

MARK SENLOOP
MODE
COPY M X
TEST X = -1
TJMP END
MODE
REPL SENRUN
@REP 10
COPY F M
@END
JUMP SENLOOP

MARK END
WIPE

MARK PRESRUN
LINK -1
SWIZ X 3 T
ADDI T 800 T
LINK T
SWIZ X 2 T
ADDI T 200 T
GRAB T
SWIZ X 1 T
MULI T 10 T
SEEK T
@REP 10
COPY F M
@END
HALT

MARK SENRUN
LINK -1
SWIZ X 3 T
ADDI T 800 T
LINK T
SWIZ X 2 T
ADDI T 200 T
GRAB T
SWIZ X 1 T
MULI T 10 T
SEEK T
@REP 10
COPY M F
@END
```