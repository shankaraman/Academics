#!/bin/sh

if [ $# -ne 3 ]
then
    value=`expr $# + 1`
    while [ $value -le 3 ]
    do
        echo "Argument Number:"
        read num
        set $* $num
        value=`expr $value + 1`
    done
fi
echo "The Value is:"$*
