___
# meta and meta-framing framework
## a mf cool minimalist/modular tool
### tested on: windows mac ubuntu centos wsl
- meta-framing
- log tool w/cron
   -
- meta management (exif and json)
- misc tools
~~~
rewriting another project of mine on: github.com/rightthumb
~~~
___
## drill down a little
- meta management
   - folder
   - file
- other tool
   - website management
   - backups

### edits exif but uses json files internally
- abbreviation features
   - switches
      - use: -save or -s
      - use: -file of -f
   - table column names for sorting and

___
## examples
~~~sh
## bookmarks
mf m docs  # save bookmark to current folder
mf b docs  # takes you to the the previously specified folder

mf  [ fi -r + *.doc -ago 1w ] # colorized list of path (full or relative ) and total
mf  [ fi -r -type doc -ago 1w  ] # .doc .docx .pdf etc
mf  [ fi -r -type image -ago 1h  ] # .jpg .png .bmp etc
mf  [ fi -r -type graphic -ago 10min  ] # .psd .tif

## misc examples
mf  [ fi -type graphic -ago 10min -scan { location:unknown, scan: quick } ]
mf  [ fi -type graphic -ago 10min -scan { location:unknown, scan: smart, promiscuous, projects.db, paths.txt } ]
mf  [ fi -r + *.py - { path:bk, fo:foo bar } -save file_meta.json file_meta.db ]
mf  [ db -f file_meta.db + *.psd ]
mf  [ traverse -f file_meta.json -index ]
mf  [ traverse -f Ability-Scores.json -search i.name i.skills.name ]
mf  [ traverse -f spells.json -search classes~Sorcerer "name=Chill Touch" -field description ] [ dice_scan ]

# help examples
## notice the location of the ?
mf  [ fi ? ] # help about module
mf  [ fi -type graphic -ago 10min -scan { scan: smart ? } ] # help on scan:smart and instructions how to add folders to the index
mf  [ fi -type graphic -ago 10min -scan { scan: smart } ? ] # help about switches specified


~~~
___
### download the whole thing
### or
### download one file (mf.py)
~~~
if you download just mf.py

it will download what it needs
and install what it needs
(asking is not default but can be changed)
~~~
___