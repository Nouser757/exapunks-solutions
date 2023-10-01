# 5: Euclid's Pizza (Order System)
<div align='center'><img src='PB003B.gif' /></div>
n
## Instructions
>Append your order (file 300) to the end of the order list (file 200).
>
>Note that all orders, including yours, will consist of exactly five keywords.

## Solution

### [XA](XA.exa) (GLOBAL)
```asm
LINK 800
LINK 800
LINK 805
MARK LOOP
COPY 0 #POWR
COPY 1 #POWR
JUMP LOOP
```