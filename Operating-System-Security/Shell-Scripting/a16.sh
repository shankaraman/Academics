#!/bin/sh

echo "Please Enter the following commands alone |who,cal,ls,ps|"
read command

case $command in
    who) who;;
    cal) cal;;
    ls) ls;;
    ps) ps;;
    *) echo "Please enter the following commands alone |who,cal,ls,ps|"
esac
