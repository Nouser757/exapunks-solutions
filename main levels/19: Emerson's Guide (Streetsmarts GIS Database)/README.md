# 19: Emerson's Guide (Streetsmarts GIS Database)
<div align='center'><img src='PB018.gif' /></div>

## Instructions
>Each host contains a list of restaurants and their ratings, from one to five stars (file 200). Locate the entry that corresponds to the Last Stop on Eddy Street and change its rating from one to five stars.
>
>The name of the target restaurant and its location within the GIS grid is available in file 300. The first coordinate is the number of times to move east, while the second coordinate is the number of times to move north (positive) or south (negative).
>
>For more information see "Network Exploration: Geographic Information Systems" in the second issue of the zine.

## Solution

### [XA](XA.exa) (GLOBAL)
```asm
GRAB 300
LINK 800
SEEK 1
COPY F X
MARK EAST
TEST X = 0
TJMP NOSO
LINK 801
SUBI X 1 X
JUMP EAST
MARK NOSO
COPY F X
TEST X < 0
TJMP SOUTH
MARK NORTH
TEST X = 0
TJMP GRAB
LINK 800
SUBI X 1 X
JUMP NORTH
MARK SOUTH
TEST X = 0
TJMP GRAB
LINK 802
ADDI X 1 X
JUMP SOUTH
MARK GRAB
SEEK -9999
COPY F X
WIPE
GRAB 200
MARK SEEK
TEST F = X
TJMP WRITE
SEEK 5
JUMP SEEK
MARK WRITE
COPY F X
@REP 4
COPY X F
@END
```