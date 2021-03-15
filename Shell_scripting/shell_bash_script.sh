#!/usr/bin/bash
# The above tells the shell that this is a Bash script, and that it should be run as such.
#*************************************************************************************
echo "hi"
# now via the main terminal or the vscode terminal, in order to execute that:
# 1. go the path of this script
# 2. chmod +x filename.sh
# 3. ./filename.sh
#
# or just via the terminal: $ bash filename.sh
#*************************************************************************************
VALUE="foo"
# 2 ways to print:
echo "$VALUE"
echo "${VALUE}"
#*************************************************************************************
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
#*************************************************************************************
# for-loop
BRANDS="benz audi volvo ferrari"
for BRAND in $BRANDS
    do
        echo "The brand of the car is: $BRAND"
#*************************************************************************************
echo "Bash version is: $BASH_VERSION"
#*************************************************************************************
# print numbers in range(10) with step 2:
echo {1..10..2}