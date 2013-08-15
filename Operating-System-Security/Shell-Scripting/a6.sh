#!/bin/sh
echo "Enter the name of the file:"
read files
ls -R | find  -name $files
