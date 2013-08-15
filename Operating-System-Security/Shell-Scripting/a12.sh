#!/bin/sh
touch hello.txt
perl -e "print 'while'x50" > hello.txt
echo "Original File:"
cat hello.txt
echo "\nAfter replacing the word while with untill:"
sed -i 's/while/untill/g' hello.txt 
cat hello.txt
