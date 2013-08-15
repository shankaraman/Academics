#!/bin/sh

 trap 'dialog --msgbox "Script Aborted1" 6 50 ; error exit' 1 2 3 15
while true
do
    ls
    echo "Enter the filename to be deleted"
    read name
    rm $name 
done
