# parser instructions

## input
3 folders in the "in" directory, gotta fill all of them with something

### descriptions
go to [game folder]/Content/descriptions/[locale]/, and copy paste all files there into this folder

### solutions
go to your save folder:
| platform | folder
| --- | --- |
| windows | %USERPROFILE%\Documents\My Games\EXAPUNKS\<user-id>\ |
| mac os | $HOME/Library/Application Support/EXAPUNKS/<user-id>/ |
| linux | $HOME/.local/share/EXAPUNKS/<user-id>/ |

copy all .solution files there into this folder, and delete any files that belong to AXIOM networks [you can tell because they'll have a thingy after their name that starts with w or c]

### gifs
save a gif for every level you intend to parse, move it into this directory, rename it based on the name text file in this directory [e.g. euclid's pizza gif would be named "PB003B.gif"

## running
run parse.py, if it encounters multiple solutions for the same level it'll ask which one to keep, enter "1" to keep the last solution, enter "2" to keep the next one instead
