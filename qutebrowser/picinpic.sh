#!/bin/bash
# https://www.reddit.com/r/qutebrowser/comments/acx6uc/my_picture_in_picture_workaround_for_qutebrowser/
# workaround for picture in picture like chrome

Link="$1"
Launch_Options=""
Launch_Options+=" --really-quiet --fs=no --force-window"
Launch_Options+=" --volume=60"
Launch_Options+=" --autofit=30% --geometry=-10-15"
Launch_Options+=" --x11-name=Picture-in-Picture" 

Launch_cmd=(/usr/bin/mpv $Launch_Options "$Link")
"${Launch_cmd[@]}" &

