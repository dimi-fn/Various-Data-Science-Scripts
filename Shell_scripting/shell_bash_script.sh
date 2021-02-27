#!/usr/bin/bash

echo "hi"
# now via the main terminal or the vscode terminal, in order to execute that:
# 1. go the path of this script
# 2. chmod +x shell_bash_script.sh
# 3. ./shell_bash_script.sh
#
#
VALUE="foo"
# 2 ways to print:
echo "$VALUE"
echo "${VALUE}"
#
# if - then - elif-fi 
NAME="bar"
if [ $NAME=="bar" ]
then 
    echo "Your name is bar"
elif [ $NAME=="foo" ]
then    
    echo "Your name is foo"
else
    echo "I don't know your name"
fi
#
# for-loop
BRANDS="benz audi volvo ferrari"
for BRAND in $BRANDS
    do
        echo "The brand of the car is: $BRAND"