# B1: KGOG-TV (Programming Hub)
<div align='center'><img src='PB014.gif' /></div>

## Instructions
>To win this battle you must make your movies play for longer than your opponent's. A movie will play when that movie's file is the only movie file sitting in a *channel* host.
>
>     Gain one point every cycle for each of your movies that is playing (files 210 and 211).
>
>     Lose one point every cycle that a movie file that isn't yours (files 230, 231, and 265) is held by an EXA you control or is sitting in your host.
>
>     Lose one point every time one of your EXAs executes a KILL instruction.
>
>Note that you may only battle your Steam friends after beating the NPC opponent. To view the list of possible opponents, click the "SELECT OPPONENT" button above.
>
>For more information see "Hacker Battle Domination" in the second issue of the zine.

## Solution

### [XA](XA.exa) (GLOBAL)
```asm
LINK 800
KILL
NOOP
NOOP
NOOP
NOOP
NOOP
KILL
GRAB 211
LINK 828
DROP
LINK -1
GRAB 210
LINK 867
```