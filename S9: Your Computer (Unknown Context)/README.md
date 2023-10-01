# S9: Your Computer (Unknown Context)
<div align='center'><img src='PB058.gif' /></div>
n
## Instructions
>Packetize and transmit the target data (file 301) to the *internet* so that it is uploaded to a warez site (file 300).
>
>A packet is a file that consists of the source IP address (from the #ADDR register), the destination IP address (from the DNS cache, file 201), the checksum of the packet's data, and between 1 and 30 data values. The target data should be split into multiple packets so that no packet except for the last contains fewer than 30 data values.
>
>To calculate a packet's checksum, add the data values together considering each digit separately, wrapping back to 0 when a digit's sum reaches 10. Then flip the sign. For example, the checksum of 3097, 1047, and 2501 is -6535.

## Solution

### [XA](XA.exa) (GLOBAL)
```asm
GRAB 300
COPY F X
WIPE
LINK 800
LINK 885
GRAB 201
MARK FINDIP
TEST F = X
FJMP FINDIP
COPY F X
DROP
MARK LOOP
MAKE
COPY #ADDR F
COPY X F
@REP 30
COPY M F
SEEK -1
TEST F = -1
TJMP DONE
@END
MODE
REPL CHECK
SEEK -9999
SEEK 2
@REP 30
COPY F M
@END
COPY -1 M
COPY M T
SEEK -9999
REPL HELPWRITE
COPY F M
COPY F M
COPY T M
@REP 30
COPY F M
@END
WIPE
MODE
JUMP LOOP


MARK CHECK
@REP 6
NOOP
@END
MAKE
@REP 4
COPY 0 F
@END
MARK CLOOP
SEEK -9999
COPY M X
TEST X = -1
TJMP DONECHECK
@REP 4
SWIZ X @{4,-1} T
ADDI T F T
MODI T 10 T
SEEK -1
COPY T F
@END
JUMP CLOOP

MARK DONECHECK
MULI F 1000 X
MULI F 100 T
ADDI X T X
MULI F 10 T
ADDI X T X
ADDI X F X
MULI X -1 M
WIPE
HALT

MARK DONE
SEEK -1
VOID F
MODE
REPL CHECK
SEEK -9999
SEEK 2
TEST EOF
TJMP WHOOPSIES
@REP 30
COPY F M
TEST EOF
TJMP STOPCHECK
@END
MARK STOPCHECK
COPY -1 M
COPY M X
SEEK -9999
REPL HELPWRITE
COPY F M
COPY F M
COPY X M
@REP 30
COPY F M
TEST EOF
TJMP OVER
@END
MARK OVER
COPY -1 M
WIPE
HALT
MARK HELPWRITE
MAKE
@REP 33
COPY M X
TEST X = -1
TJMP HALT
COPY X F
@END
MARK HALT
LINK 800
HALT

MARK WHOOPSIES
WIPE
KILL
```

### [XB](XB.exa) (GLOBAL)
```asm
GRAB 301
MARK LOOP
@REP 30
COPY F M
TEST EOF
TJMP DONE
@END
JUMP LOOP

MARK DONE
COPY -1 M
```