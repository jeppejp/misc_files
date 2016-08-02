CURRENT_LAYOUT=$(setxkbmap -query | grep layout | cut -d " " -f 6)
echo $CURRENT_LAYOUT
