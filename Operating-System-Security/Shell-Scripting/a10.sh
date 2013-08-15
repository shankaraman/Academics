#!/bin/sh
echo "Enter the name of the file"
read ya
if [ -f "$ya" ]
then
    echo "File Exists!"
elif [ -d "$ya" ]
then
    echo "Directory Exists!"
else 
    echo "No files or Directory found!"
fi
