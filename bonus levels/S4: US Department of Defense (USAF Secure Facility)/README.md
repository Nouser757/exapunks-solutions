# S4: US Department of Defense (USAF Secure Facility)
<div align='center'><img src='PB056.gif' /></div>

## Instructions
>﻿Find the unredacted version of the ‗PROJECT OGRE‗ report (file 300), make a copy of it, and bring the copy back to your host. The target file will be behind one or more locks, which each require a three-digit code.
>
>Since this task takes place inside a network run by the military it includes additional security features not found in other networks. You may not have more than one EXA in the network at a time, and you may not use the M register to communicate between an EXA in the network and an EXA in your host.

## Solution

### [BF](BF.exa) (GLOBAL)
```asm
MARK BF1
LINK 800
COPY X #LOCK
LINK -1
REPL RUN1
@REP 4
NOOP
@END
ADDI X 1 X
JUMP BF1

MARK RUN1
LINK 800
LINK 800
LINK -1
LINK -1
KILL
COPY 0 X

MARK BF2
LINK 800
LINK 800
COPY X #LOCK
LINK -1
LINK -1
REPL RUN2
@REP 6
NOOP
@END
ADDI X 1 X
JUMP BF2

MARK RUN2
LINK 800
LINK 800
LINK 800
LINK -1
LINK -1
LINK -1
KILL
GRAB 300
COPY F X
WIPE
LINK 800
@REP 2
LINK @{801,1}
GRAB 200
TEST F = X
TJMP FOUND@{1,1}
DROP
LINK -1
@END
LINK 800
@REP 4
LINK @{801,1}
GRAB 200
TEST F = X
TJMP FOUND@{3,1}
DROP
LINK -1
@END
LINK 800
@REP 2
LINK @{801,1}
GRAB 200
TEST F = X
TJMP FOUND@{7,1}
DROP
LINK -1
@END

@REP 2
MARK FOUND@{1,1}
DROP
LINK -1
LINK -1
MAKE
COPY X F
DROP
COPY 1 X
JUMP WRITELOOP@{1,1}
@END

@REP 4
MARK FOUND@{3,1}
DROP
LINK -1
LINK -1
LINK -1
MAKE
COPY X F
DROP
COPY 1 X
JUMP WRITELOOP@{3,1}
@END

@REP 2
MARK FOUND@{7,1}
DROP
LINK -1
LINK -1
LINK -1
LINK -1
MAKE
COPY X F
DROP
COPY 1 X
JUMP WRITELOOP@{7,1}
@END

@REP 2
MARK WRITELOOP@{1,1}
LINK 800
LINK @{801,1}
GRAB 200
SEEK X
TEST EOF
TJMP DONE
COPY F T
DROP
LINK -1
LINK -1
GRAB 400
SEEK X
COPY T F
ADDI X 1 X
DROP
JUMP WRITELOOP@{1,1}
@END

@REP 4
MARK WRITELOOP@{3,1}
LINK 800
LINK 800
LINK @{801,1}
GRAB 200
SEEK X
TEST EOF
TJMP DONE
COPY F T
DROP
LINK -1
LINK -1
LINK -1
GRAB 400
SEEK X
COPY T F
ADDI X 1 X
DROP
JUMP WRITELOOP@{3,1}
@END

@REP 4
MARK WRITELOOP@{7,1}
LINK 800
LINK 800
LINK 800
LINK @{801,1}
GRAB 200
SEEK X
TEST EOF
TJMP DONE
COPY F T
DROP
LINK -1
LINK -1
LINK -1
LINK -1
GRAB 400
SEEK X
COPY T F
ADDI X 1 X
DROP
JUMP WRITELOOP@{7,1}
@END


MARK DONE
```