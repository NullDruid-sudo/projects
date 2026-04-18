!/bin/bash
echo "Enter no to check positive or negative"
read x
if [[ $x -gt 0 ]];
then
        echo "$x is positive "
elif [[ $x -eq 0 ]];
then
        echo "$x is neither positive nor negative"
else
        echo "$x is neative"
fi
