# 16: TEC Redshift (Development Kit)
<div align='center'><img src='PB015.gif' /></div>
n
## Instructions
>There is an unknown three-digit code (such as 4-7-3) that, when entered one digit at a time into #PASS, will unlock the link between *debug* and *secret*. Find the three-digit code and create a file in your host that contains the code as a sequence of three values, followed by the development kit's RDK ID.

## Solution

### [TS](TS.exa) (GLOBAL)
```asm
LINK 800
MARK LOOP
SWIZ X 1 #PASS
SWIZ X 2 #PASS
SWIZ X 3 #PASS
REPL TEST
ADDI X 1 X
JUMP LOOP
MARK TEST
LINK 800
LINK -1
KILL
LINK 800
COPY X M
GRAB 199
COPY F M
```

### [WR](WR.exa) (GLOBAL)
```asm
MAKE
COPY M X
SWIZ X 1 F
SWIZ X 2 F
SWIZ X 3 F
COPY M F
```