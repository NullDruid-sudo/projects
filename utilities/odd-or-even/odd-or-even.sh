#!/bin/bash
read x
if [[ $((x % 2)) -eq 0 ]];
then
        echo "The given number $x is even "
elif [[ $((x*1)) -eq 0 ]];
then
        echo "The given number is zero "
else
        echo "The given number $x is odd"
fi
