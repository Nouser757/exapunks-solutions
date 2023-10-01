# S6: Española Valley High School (School Management System)
<div align='center'><img src='PB057.gif' /></div>
n
## Instructions
>﻿Replace ‗ENGLISH‗ with ‗AP ENGLISH‗ (file 300) in selenium\_wolf's child's class schedule (file 235).
>
>Because those two classes are most likely not offered at the same time, you may need to rearrange the rest of their schedule to make it fit. Modify the schedule so that they are taking the same classes but at different times when necessary. A full list of classes offered is available in file 200.
>
>Note that there will only be one valid schedule. 
>
>Also note that ‗AP ENGLISH‗ will only be offered once and each other class will be offered no more than twice.

## Solution

### [TM](TM.exa) (GLOBAL)
```asm
LINK 800
GRAB 200
COPY M X
MARK SEARCHTIME
TEST F = X
FJMP SEARCHTIME
SEEK -2
TEST F = M
TJMP SKIPONE
SEEK -1
COPY F X
COPY X M
SEEK -9999
COPY M T
MODE
COPY X M
COPY M X
MODE
TEST X = T
TJMP FINAL
COPY X M
JUMP SEARCHTIME

MARK SKIPONE
COPY -1 M
SEEK 1
JUMP SEARCHTIME

MARK FINAL
COPY -69 M
MODE
COPY -69 M
```

### [MN](MN.exa) (GLOBAL)
```asm
GRAB 300
LINK 800
SEEK 1
COPY F M
COPY 0 M
COPY M X
TEST X = -1
FJMP NOSKIP1
COPY 0 M
COPY M X
MARK NOSKIP1
COPY X F
SEEK -9999
COPY F M
MARK SEARCHLOOP
SEEK 9999
COPY M X
TEST X = -69
TJMP FINAL
COPY X F
SEEK -2
COPY F M
COPY M X
TEST X = -1
FJMP NOSKIP2
SEEK -1
COPY F M
COPY M X
MARK NOSKIP2
SEEK 2
COPY X F
SEEK -9999
COPY F M
SEEK 9999
JUMP SEARCHLOOP

MARK FINAL
SEEK -9999
COPY F X
SEEK 9999
SEEK -1
MODE
MARK WRITELOOP
TEST F = X
TJMP DONE
SEEK -1
COPY F M
SEEK -2
COPY F M
SEEK -2
JUMP WRITELOOP

MARK DONE
COPY -420 M
WIPE
```

### [SC](SC.exa) (GLOBAL)
```asm
LINK 800
LINK 800
LINK 802
GRAB 235
MARK SEARCHLOOP
COPY M X
TEST X = -69
TJMP FINAL
MARK SEARCHTIME
TEST F = X
FJMP SEARCHTIME
COPY F M
SEEK -9999
JUMP SEARCHLOOP

MARK FINAL
SEEK -9999
COPY M X
TEST X = -420
TJMP DONE
MARK WRITESEARCH
TEST F = X
FJMP WRITESEARCH
COPY M F
JUMP FINAL

MARK DONE
```