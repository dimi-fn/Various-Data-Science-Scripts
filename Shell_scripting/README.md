# Contents

* [Shell Scripting](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#shell-scripting)
    * [Bash](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#bash)
        * [Commands](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#commands)
        * [Hashbang](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#hashbang)
* [Terminal - General](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#terminal---general)
    * [Bash Commands (Linux - MacOS - WSL)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#bash-commands-linux---macos---wsl)
    * [Windows Terminal Commands](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#windows-terminal-commands)

----

# Shell Scripting

`Shell scripting` is a program to run on UNIX shell, and `Bash` is a Unix shell and command language.

* The terminal can be used on Linux and Mac, the git bash on Windows

## Bash 
### Commands

* `which bash` : to know where is your bash ==> this will be the first line of code in the script after `#!`
    * e.g. if after typing "which bash" the result is "/bin/bash" then the 1st line of code should be: `#!/bin/bash`
    * in case permission is required: `chmod +x 'bash_script'.sh`

* terminal (in order to run the .sh file):
    1) go the path of the bash script (where the bashfilename.`sh` is located)
    2) `chmod +x bashfilename.sh`
    3) `./bashfilename.sh`    

* no spaces among code, it is like typing in the terminal

* `-eq` : To check if two numbers are equal

* `-ne` : To check if two number are not equal

* `-gt` : To check if num1 > num2

* `-lt` : To check if num1 < num2

* `-le` : less than equal to

### Hashbang 

`#!/usr/bin/env/ python3` ==> the **shebang line**, or **hashbang**

* `#!` --> ("hash" + "bang") 

* `usr/bin/env python3` --> the path to the executable that will run the script along with any other optional arguments

    * it is a common pattern for Unix based systems

    * it allows a script to be invoked from the command line

    * it should be in the very first line of the script

    * on Windows this line will be considered a comment and hence will be completely ignored
    * on linux of course it will not be ignored since it is Unix based, same on Mac because it is based on the BSD Unix


# Terminal - General

## Bash Commands (Linux - MacOS - WSL)

- updates: `sudo apt-get update` | `sudo apt-get upgrade`

- `reboot` / `shutdown now`

- `cd` / `cd ..` / `ls`

- Ubuntu version: `lsb_release -a` 

- create folder/directory: `mkdir "dirname"`

- delete file `rm "filename"`

- remove folder/directory:
    * if empty: `rmdir "foldername"`
    * if non-empty: `rm -r "foldername"`

- open file: `xdg-open "filename"`

- python version: `python3 --version`

- clear terminal: `clear`

- ip details `nmcli device show`

- disc space `ncdu`


## Windows Terminal Commands

- `cd` / `cd ..` / `dir`

- clear terminal: `cls`

- create folder/directory : `mkdir "directory name"`

- cut and paste file `move "doc.txt" C:\path`

- delete folder:
    * `rmdir ""`
    * `rmdir ""` /s (if it has files inside)

- delete file: `del /f "filename"`

- ip details: `ipconfig`


-----

### Sources

[1] https://www.linkedin.com/learning/python-essential-training-2018/

[2] https://medium.com/@saswat.sipun/shell-scripting-cheat-sheet-c0ecfb80391

[3] https://help.ubuntu.com/community/Beginners/BashScripting

[4] https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo