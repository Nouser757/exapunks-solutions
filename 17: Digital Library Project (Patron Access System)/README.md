# 17: Digital Library Project (Patron Access System)
<div align='center'><img src='PB016.gif' /></div>
n
## Instructions
>Books are stored in the host corresponding to the first digit of their call number, while a book's file ID is 200 plus the last two digits of the call number. For example, book 512 would be stored in the host *500-599* as file 212.
>
>Duplicate each of the books requested by EMBER-2 and bring them back to your host.
>
>The call numbers for the books EMBER-2 wants are available in file 300.
>
>Note that EMBER-2 will never request more than one book from the same host.

## Solution

### [RD](RD.exa) (LOCAL)
```asm
GRAB 300
LINK 800
MARK READ
COPY F X
MODE
REPL RUN
MODE
VOID M
TEST EOF
TJMP HALT
JUMP READ
MARK RUN
LINK 800
SUBI X 100 X
TEST X < 100
FJMP RUN
ADDI X 200 X
GRAB X
MARK SEND
TEST EOF
TJMP OVER
COPY F M
JUMP SEND
MARK OVER
COPY -420 M
HALT
MARK HALT
WIPE
MODE
COPY -6969 M
```

### [WR](WR.exa) (GLOBAL)
```asm
MARK START
MAKE
MARK WRITE
COPY M X
TEST X = -420
TJMP NEXT
TEST X = -6969
TJMP HALT
COPY X F
JUMP WRITE
MARK NEXT
DROP
LINK 800
MODE
COPY -1 M
MODE
LINK -1
JUMP START
MARK HALT
```