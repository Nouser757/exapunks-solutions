# B5: Aberdeen (selenium_wolf)
<div align='center'><img src='PB031B.gif' /></div>
n
## Instructions
>To win this battle you must occupy a majority of the hosts for as long as possible. You occupy a host if you have more EXAs in it than your opponent.
>
>     Gain one point every cycle you occupy more hosts than your opponent.
>
>     Lose one point every time one of your EXAs executes a KILL instruction.
>
>Writing any value to the #NUKE register will destroy all EXAs in that host, including the EXA that triggered it.
>
>For more information see "Hacker Battle Domination" in the second issue of the zine.

## Solution

### [XA](XA.exa) (GLOBAL)
```asm
LINK 800
REPL SLOOP
REPL 802
JUMP SLOOP

MARK 802
LINK 802
REPL 800
REPL SLOOP
JUMP SLOOP

MARK 800
LINK 800
REPL 800
REPL SLOOP
JUMP SLOOP

MARK SLOOP
JUMP SLOOP
```

### [XB](XB.exa) (GLOBAL)
```asm
LINK 800
LINK 801
LINK 799
MARK SLOOP
JUMP SLOOP
```