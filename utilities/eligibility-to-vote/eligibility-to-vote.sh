#!/bin/bash
echo "Enter age"
read x
if [[ x -ge 18 ]];
then
        echo "Eligible to vote "
else
        echo "not Eligible to vote"
fi
