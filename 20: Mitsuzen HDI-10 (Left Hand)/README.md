# 20: Mitsuzen HDI-10 (Left Hand)
<div align='center'><img src='PB038.gif' /></div>
n
## Instructions
>There are three nerve signals that need to be relayed: muscle control (M), which runs from your central nervous system (CNS) to your hand (HND), and heat (H) and pressure (P), which run the other direction.
>
>For each signal, read a value from the input nerve and relay it to the output nerve. Repeat _ad infinitum_.
>
>It is not necessary to leave no trace. Your EXAs should be written to operate indefinitely.
>
>For more information see "Debugging the Phage" in the first issue of the zine.

## Solution

### [XM](XM.exa) (GLOBAL)
```asm
LINK 800
LINK -3
LINK -3
MARK LOOP
COPY #NERV X
@REP 4
LINK 3
@END
COPY X #NERV
@REP 4
LINK -3
@END
JUMP LOOP
```

### [XH](XH.exa) (GLOBAL)
```asm
LINK 800
@REP 3
LINK 3
@END
MARK LOOP
COPY #NERV X
@REP 6
LINK -3
@END
COPY X #NERV
@REP 6
LINK 3
@END
JUMP LOOP
```

### [XP](XP.exa) (GLOBAL)
```asm
LINK 800
@REP 4
LINK 3
@END
MARK LOOP
COPY #NERV X
@REP 8
LINK -3
@END
COPY X #NERV
@REP 8
LINK 3
@END
JUMP LOOP
```