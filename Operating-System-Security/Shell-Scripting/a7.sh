#!/bin/sh
touch file1
touch file2
touch file3
echo "Enter Name:"
read file1
echo "Enter file2:"
read file2
echo "Enter file3:"
read file3
cat<$file1
cat>$file2
cat>$file3
