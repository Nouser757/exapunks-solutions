# 14: Mitsuzen HDI-10 (Heart)
<div align='center'><img src='PB011B.gif' /></div>

## Instructions
>Read a value from the nerve connected to your central nervous system (CNS) and make your heart beat by writing a sequence of values to your sinoatrial (SA-N) and atrioventricular (AV-N) nodes as indicated in the HDI-10 I/O log when holding the "SHOW GOAL" button. The length of each sequence of values should be equal to the value from the CNS divided by -10. Repeat _ad infinitum_.
>
>It is not necessary to leave no trace. Your EXAs should be written to operate indefinitely.
>
>For more information see "Debugging the Phage" in the first issue of the zine.

## Solution

### [SA](SA.exa) (GLOBAL)
```asm
LINK 800
LINK 1
LINK 1
MARK LOOP
SUBI M 1 X
COPY 40 #NERV
MARK WRITE
TEST X = 0
TJMP LOOP
COPY -70 #NERV
SUBI X 1 X
JUMP WRITE
```

### [AV](AV.exa) (GLOBAL)
```asm
LINK 800
LINK 3
LINK 3
MARK LOOP
SUBI M 2 X
COPY -70 #NERV
COPY 40 #NERV
MARK WRITE
TEST X = 0
TJMP WAIT
COPY -70 #NERV
SUBI X 1 X
JUMP WRITE
MARK WAIT
NOOP
NOOP
NOOP
JUMP LOOP
```

### [CN](CN.exa) (GLOBAL)
```asm
LINK 800
MARK LOOP
DIVI #NERV -10 X
COPY X M
COPY X M
JUMP LOOP
```