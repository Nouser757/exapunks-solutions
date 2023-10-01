# 29: Mitsuzen HDI-10 (Visual Cortex)
<div align='center'><img src='PB030.gif' /></div>

## Instructions
>Read a value from each of the optic nerves present and write the correct value to the nerve that runs deeper into your visual cortex (V-CTX). To determine the value that should be written, count the number of values read that are greater than -55, multiply that count by 5, and then subtract 75. Repeat _ad infinitum_.
>
>It is not necessary to leave no trace. Your EXAs should be written to operate indefinitely.
>
>For more information see "Debugging the Phage" in the first issue of the zine.

## Solution

### [XA](XA.exa) (GLOBAL)
```asm
LINK 800
LINK 1
LINK 3
MARK LOOP
COPY 0 X
LINK -3
REPL WEST
REPL EAST
TEST #NERV > -55
FJMP C2
ADDI X 1 X
MARK C2
LINK -3
TEST #NERV > -55
FJMP C3
ADDI X 1 X
MARK C3
LINK -3
TEST #NERV > -55
FJMP COUT
ADDI X 1 X
MARK COUT
LINK 3
LINK 3
LINK 3
ADDI X M X
ADDI X M X
MULI X 5 X
SUBI X 75 X
COPY X #NERV
JUMP LOOP

MARK WEST
LINK -1
TEST #NERV > -55
FJMP W2
ADDI X 1 X
MARK W2
LINK -3
TEST #NERV > -55
FJMP W3
ADDI X 1 X
MARK W3
LINK -3
TEST #NERV > -55
FJMP WOUT
ADDI X 1 X
MARK WOUT
COPY X M
HALT

MARK EAST
LINK 1
TEST #NERV > -55
FJMP E2
ADDI X 1 X
MARK E2
LINK -3
TEST #NERV > -55
FJMP E3
ADDI X 1 X
MARK E3
LINK -3
TEST #NERV > -55
FJMP EOUT
ADDI X 1 X
MARK EOUT
COPY X M
HALT
```