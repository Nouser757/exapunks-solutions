# 32: Unknown Network 2 (Unknown Context)
<div align='center'><img src='PB034.gif' /></div>

## Instructions
>Terminate all other EXAs and bring any files they were holding back to your host. Only EXAs in the central host will be holding files, and their file IDs will always be between 200 and 299, inclusive.
>
>Note that some links may become non-traversable as a result of your actions.

## Solution

### [XA](XA.exa) (GLOBAL)
```asm
@REP 5
LINK 800
@END
@REP 6
KILL
@END
COPY 200 X
MARK GRABLOOP
REPL GRABRUN
ADDI X 1 X
TEST X = 300
FJMP GRABLOOP
LINK -1
@REP 4
KILL
LINK -1
REPL KAMIKAZE
@END
HALT

MARK GRABRUN
GRAB X
@REP 5
LINK -1
@END
HALT

MARK KAMIKAZE
LINK 800
KILL
```