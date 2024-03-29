# S7: Mitsuzen D300-N (Personal Storage Array)
<div align='center'>[sorry no gif for this one it was 300mb and 34 minutes long]</div>
<div align='center'>[cycles: 64641 | size: 443 | activity: 6255]</div>

## Instructions
>The data on this drive array is duplicated across three drives for redundancy, with a file name index stored in the *controller* (file 200). Unfortunately, the drive array is failing.
>
>For each file stored in the drive array, create a file in your host that contains the file name and data. Some values are corrupted and will read as a keyword (‗FAIL‗) instead of a number. You will need to read these values from a different drive that is not corrupted.
>
>Note that some links may be unreliable as a result of the drive array's impending failure.

## Solution

### [XA](XA.exa) (GLOBAL)
```asm
LINK 800
MAKE
DROP
GRAB 200
MARK LOOP
TEST EOF
TJMP DONE
COPY F X
COPY F M
REPL RUN1
REPL RUN2
REPL RUN3
REPL RUN1
REPL RUN2
REPL RUN3
REPL RUN1
REPL RUN2
REPL RUN3
REPL RUN1
REPL RUN2
REPL RUN3
REPL RUN1
REPL RUN2
REPL RUN3
REPL RUN1
REPL RUN2
REPL RUN3
REPL RUN1
REPL RUN2
REPL RUN3
REPL RUN1
REPL RUN2
REPL RUN3
JUMP LOOP

MARK RUN1
LINK 801
GRAB X
MODE
MARK SENDLOOP1
TEST MRD
FJMP SENDLOOP1
COPY M X
@REP 40
NOOP
@END
TEST X = -1
TJMP HALT
TEST X = 1
TJMP SEND1
TEST X = 0
TJMP RESET1
JUMP SENDLOOP1
MARK SEND1
TEST EOF
TJMP END1
COPY F X
SEEK -1
@REP 16
REPL CROSS
@END
JUMP SENDLOOP1
MARK RESET1
SEEK 1
JUMP SENDLOOP1
MARK END1
COPY -9999 X
@REP 16
REPL CROSS
@END
HALT

MARK RUN2
LINK 802
GRAB X
MODE
MARK SENDLOOP2
TEST MRD
FJMP SENDLOOP2
COPY M X
@REP 40
NOOP
@END
TEST X = -1
TJMP HALT
TEST X = 2
TJMP SEND2
TEST X = 0
TJMP RESET2
JUMP SENDLOOP2
MARK SEND2
TEST EOF
TJMP END2
COPY F X
SEEK -1
@REP 16
REPL CROSS
@END
JUMP SENDLOOP2
MARK RESET2
SEEK 1
JUMP SENDLOOP2
MARK END2
COPY -9999 X
@REP 16
REPL CROSS
@END
HALT


MARK RUN3
LINK 803
GRAB X
MODE
MARK SENDLOOP3
TEST MRD
FJMP SENDLOOP3
COPY M X
@REP 40
NOOP
@END
TEST X = -1
TJMP HALT
TEST X = 3
TJMP SEND3
TEST X = 0
TJMP RESET3
JUMP SENDLOOP3
MARK SEND3
TEST EOF
TJMP END3
COPY F X
SEEK -1
@REP 16
REPL CROSS
@END
JUMP SENDLOOP3
MARK RESET3
SEEK 1
JUMP SENDLOOP3
MARK END3
VOID M
VOID M
COPY -9999 X
@REP 16
REPL CROSS
@END
HALT

MARK CROSS
LINK -1
GRAB 400
MODE
@REP 40
NOOP
@END
DROP
LINK -1
COPY X M
HALT


MARK DONE
COPY -1 M
DROP
GRAB 400
WIPE
MARK HALT
```

### [XB](XB.exa) (GLOBAL)
```asm
MARK LOOP
LINK 800
COPY M X
TEST X = -1
TJMP DONE
LINK -1
MAKE
COPY X F
MODE
MARK RECVLOOP
COPY 1 M
COPY 1 M
COPY 1 M
MODE
COPY M X
MODE
TEST X > -1
FJMP FAIL1
COPY X F
COPY 0 M
COPY 0 M
COPY 0 M
JUMP RECVLOOP
MARK FAIL1
COPY 2 M
COPY 2 M
COPY 2 M
MODE
COPY M X
MODE
TEST X > -1
FJMP FAIL2
COPY X F
COPY 0 M
COPY 0 M
COPY 0 M
JUMP RECVLOOP
MARK FAIL2
COPY 3 M
COPY 3 M
COPY 3 M
MODE
COPY M X
MODE
TEST X > -1
FJMP FAIL3
COPY X F
COPY 0 M
COPY 0 M
COPY 0 M
JUMP RECVLOOP
MARK FAIL3
DROP
MODE
JUMP LOOP

MARK DONE
```
