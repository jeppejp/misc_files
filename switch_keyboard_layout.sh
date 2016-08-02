CURRENT_LAYOUT=$(setxkbmap -query | grep layout | cut -d " " -f 6)

if [[ "$CURRENT_LAYOUT" == gb ]]
    then
        setxkbmap dk
    else
        setxkbmap gb
fi
