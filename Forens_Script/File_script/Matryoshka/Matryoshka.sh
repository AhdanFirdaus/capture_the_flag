#!/bin/bash
LIMIT=500  #number of cycles
for ((i=1; i <= LIMIT ; i++)) do
# find . -name '*.rar' -exec unrar e {} \; -exec rm {} \; #rar file
# find . -name '*.7z' -exec 7za e {} \; -exec rm {} \; # 7z file
# find . -name '*.zip' -exec unzip {} \; -exec rm {} \; #zip file
done

#recursive file rar,zip,7z you can open the files with this script.
