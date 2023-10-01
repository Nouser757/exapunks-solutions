# 6: Mitsuzen HDI-10 (Left Arm)
<div align='center'><img src='PB004.gif' /></div>

## Instructions
>Read a value from the nerve connected to your central nervous system (CNS) and relay it to the nerve connected to your arm (ARM), clamping the value so that it never goes below -120 or above 50. Repeat _ad infinitum_.
>
>Since this task takes place inside a network you control— that is, your own body— it is not necessary to leave no trace. Your EXAs should be written to operate indefinitely.
>
>Note that #NERV is a _hardware register_, not a file. You can use it directly in your code like any other register.
>
>For more information about the phage see "Debugging the Phage" in the first issue of the zine.

## Solution

### [RC](RC.exa) (GLOBAL)
```asm
LINK 800
@REP 4
LINK 1
@END
MARK LOOP
COPY M X
TEST X > 50
TJMP HICLAMP
MARK SEND
COPY X #NERV
JUMP LOOP
MARK HICLAMP
COPY 50 X
JUMP SEND
```

### [SN](SN.exa) (GLOBAL)
```asm
LINK 800
MARK LOOP
COPY #NERV X
TEST X < -120
TJMP LOCLAMP
MARK SEND
COPY X M
JUMP LOOP
MARK LOCLAMP
COPY -120 X
JUMP SEND
```