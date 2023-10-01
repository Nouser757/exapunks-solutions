# 33: TEC EXA-Blaster Modem (Pager Network)
<div align='center'><img src='PB035B.gif' /></div>
n
## Instructions
>Connect to each pager and copy EMBER-2's message (file 300) to the screen (#DATA). Then activate all of the pagers at exactly the same time by writing a value to each #PAGE register in the same cycle.
>
>A list of phone numbers for the pagers is available in file 301.
>
>For more information see "Hacker Skills: Modem Control at the Direct Level" in the second issue of the zine.


## Solution

### [DI](DI.exa) (LOCAL)
```asm
GRAB 301
LINK 800
MARK LOOP
COPY -1 #DIAL
@REP 11
COPY F #DIAL
@END
REPL RUN
VOID M
JUMP LOOP

MARK RUN
MODE
LINK 800
MARK WLOOP
COPY M X
TEST X = -1
TJMP WAIT
COPY X #DATA
JUMP WLOOP

MARK WAIT
COPY M X
MARK SLEEP
ADDI X 1 X
TEST X = 128
TJMP FIRE
JUMP SLEEP

MARK FIRE
COPY 69 #PAGE
```

### [RD](RD.exa) (GLOBAL)
```asm
GRAB 300
LINK 800
MARK RLOOP
COPY F M
TEST EOF
FJMP RLOOP
SEEK -9999
COPY -1 M
COPY X M
MODE
COPY 200 M
MODE
ADDI X 16 X
TEST X = 128
TJMP HALT
JUMP RLOOP
MARK HALT
WIPE
GRAB 301
WIPE
```