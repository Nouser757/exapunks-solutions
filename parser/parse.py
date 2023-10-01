import os
import shutil

doneIDs = []

lookup = {"PB000": ["tutorial-1","01: Trash World News (Tutorial 1)"],
"PB001": ["tutorial-2","02: Trash World News (Tutorial 2)"],
"PB037": ["tutorial-3","03: Trash World News (Tutorial 3)"],
"PB002": ["tutorial-4","04: Trash World News (Tutorial 4)"],
"PB003B": ["pizza-delivery","05: Euclid's Pizza (Order System)"],
"PB004": ["nerve-bridge","06: Mitsuzen HDI-10 (Left Arm)"],
"PB005": ["peanut-blast","07: Last Stop Snaxnet (Factory 11)"],
"PB006B": ["copy-shop","08: Zebros Copies (Point-Of-Sale System)"],
"PB007": ["highway-sign","09: SFCTA Highway Sign #4902 (Remote Access Interface)"],
"PB008": ["ghost-network","10: Unknown Network 1 (Unknown Context)"],
"PB009": ["solitaire-get","11: UC Berkeley (EECS Department)"],
"PB010B": ["workhouse-2","12: Workhouse (Work Management System)"],
"PB012": ["atm","13: Equity First Bank (San Fancisco)"],
"PB011B": ["heartbeat","14: Mitsuzen HDI-10 (Heart)"],
"PB013C": ["find-replace","15: Trash World News (Unknown Context)"],
"PB014": ["battle-1","B1: KGOG-TV (Programming Hub)"],
"PB015": ["sandbox-get","16: TEC Redshift (Development Kit)"],
"PB016": ["library","17: Digital Library Project (Patron Access System)"],
"PB040": ["radio-station","18: TEC EXA-Blaster Modem (Radio Stations)"],
"PB018": ["restaurant","19: Emerson's Guide (Streetsmarts GIS Database)"],
"PB027": ["battle-2","B2: Valhalla (=Plastered)"],
"PB038": ["left-hand","20: Mitsuzen HDI-10 (Left Hand)"],
"PB020": ["arcade-get","21: Sawayama Wonderdisc (Drive Controller)"],
"PB021": ["power-grid","22: Alliance Power and Light (Streetsmarts GIS Database)"],
"PB022": ["battle-3","B3: Deadlock's Domain (Deadlock)"],
"PB023": ["baseball","23: Xtreme League Baseball (Player Database)"],
"PB024": ["mmo","24: King's Ransom Online (US West Realm)"],
"PB028": ["satellite","25: KGOG-TV (Satellite Uplink)"],
"PB025": ["bank","26: Equity First Bank (San Francisco (ATMs Offline)"],
"PB019": ["battle-4","B4: The Wormhole (X10X10X)"],
"PB026B": ["worm","27: TEC EXA-Blaster Modem (Dataphone Network)"],
"PB029B": ["snaxnet","28: Last Stop Snaxnet (Warehouse 27)"],
"PB030": ["edge-detection","29: Mitsuzen HDI-10 (Visual Cortex)"],
"PB032": ["credit-card","30: Holman Dynamics (Sales System)"],
"PB031B": ["battle-5","B5: Aberdeen (selenium_wolf)"],
"PB033": ["dna","31: US Government (Fema Genetic Database)"],
"PB034": ["secure-enclave","32: Unknown Network 2 (Unknown Context)"],
"PB035B": ["pagers","33: TEC EXA-Blaster Modem (Pager Network)"],
"PB036": ["interface","34: Mitsuzen HDI-10 (Cerebral Cortex)}"],
"PB054": ["bonus-mutex","S1: Bloodlust Online (US East Realm)"],
"PB053": ["bonus-nth","S2: Motor Vehicle Administration (Scheduling System)"],
"PB050": ["bonus-ghast","S3: Cybermyth Studios (Accounting System)"],
"PB056": ["bonus-hydro","S4: US Department of Defense (USAF Secure Facility)"],
"PB051": ["bonus-plastered","S5: Netronics NET40 Modem (The Wardialer)"],
"PB057": ["bonus-selenium","S6: Española Valley High School (School Management System)"],
"PB052": ["bonus-x10","S7: Mitsuzen D300-N (Personal Storage Array)"],
"PB055": ["bonus-deadlock","S8: Crystalair International (Ticketing System)"],
"PB058": ["bonus-moss","S9: Your Computer (Unknown Context)"]}

for file in os.listdir(r"in/solutions"):
    with open(f"in/solutions/{file}", "rb") as f:
        x = True
        EXAs = []
        f.seek(8, 1)
        ID = [f.read(1) for _ in range(6)]
        if ID[-1] not in [b'B', b'C']:
            ID.pop()
        ID = b''.join(ID).decode()
        if ID in doneIDs:
            choice = input(f"Alternative solution found for {lookup[ID][1]}, accept former or latter solution? (1/2)>")
            while choice not in ["1", "2"]:
                choice = input(f"Alternative solution found for {lookup[ID][1]}, accept former or latter solution? (1/2)>")
            if choice == 1: continue
        else: doneIDs.append(ID)
        while x != b'':
            x = f.read(1)
            if x == b'\x0a':
                if f.read(1) != b'\x02': continue
                f.seek(3, 1)
                name = f.read(2)
                f.seek(4, 1)
                buffer = []
                while True:
                    b = f.read(1)
                    if b == b'\x00': break
                    buffer.append(b)
                mode = 'GLOBAL' if f.read(1) == b'\x00' else 'LOCAL'
                EXAs.append([name.decode(), mode, b''.join(buffer).decode()])
    with open(f"in/descriptions/{lookup[ID][0]}.txt") as f:
        description = [">" + x for x in f.readlines()]

    if not os.path.exists(f"out/{lookup[ID][1]}"):
        os.makedirs(f"out/{lookup[ID][1]}")
    with open(f"out/{lookup[ID][1]}/README.md", "w") as f:
        f.write(f"# {lookup[ID][1]}\n<div align='center'><img src='{ID}.gif' /></div>\n\n## Instructions\n{''.join(description)}\n\n## Solution\n\n" + '\n\n'.join([f"### [{x[0]}]({x[0]}.exa) ({x[1]})" + "\n```asm\n" + x[2] + '\n```' for x in EXAs]))
    
    for EXA in EXAs:
        with open(f"out/{lookup[ID][1]}/{EXA[0]}.exa", "w") as f:
            f.write(EXA[2])
    
    shutil.copyfile(f"in/gifs/{ID}.gif", f"out/{lookup[ID][1]}/{ID}.gif")