#!/bin/sh
sum=0
counter=1

while [ $counter -le 100 ]
do
    sum=`expr $sum + $counter`
    counter=`expr $counter + 1`
done
echo "The Sum of 100 no's is" $sum
