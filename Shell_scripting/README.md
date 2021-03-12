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

* updates: `sudo apt-get update` | `sudo apt-get upgrade`

* `reboot` / `shutdown now` / `systemctl suspend` / `systemctl hibernate`

* Ubuntu version: `df-h` `lsb_release -a` 

* `cd` / `cd ..` 

* `ls`
    * display all folders and subfolders and files in a tree diagram: `tree <dirname>` (first install `sudo apt install tree`)
    * recursive output: `ls -R`

* the manual page of a command and guidance info for commands: `man <command>` e.g.: `$ man ls`
    * `tldr <command>`: quick guidance info for commands, e.g. '$ tldr ls'

* locate where you are: `pwd`

* clear terminal: `clear`

* disc space / hard drive: `ncdu`

* ip details `nmcli device show`


<br>

* open file/directory/application `open <file_name>` `open <dir_name>` `open <app_name>`


<br>


* create directory (folder): `mkdir "dirname"`
    * create two folders in one command: `mkdir <dir1> <dir2>` 
    * create folder and nested subfolders: `mkdir -p <main_folder>/<subfolder>`

* delete directory
    * if dir is empty: `rmdir <dirname>` / `rmdir <dir1> <dir2>`
    * if dir is not empty: `rm -rf <non_empty_folder>` / `rm -rf <non_empty_folder> <another_non_empty_folder>`

* copy a folder: `cp -r <folder_to_be_copied> <renamed_copied_and_pasted_folder>`: 



<br>

* create file: `touch <filename>`

* copy a file: `cp <file_to_be_copied> <renamed_copied_and_pasted_file>`

* move file (like cut and paste): `mv <file_to_be_moved> <dir_destination>`

* delete file: `rm <filename>`

* open file: `xdg-open <filename>`


<br>


* find files based on extension: `find . -name '*.txt'` ==> It finds all the files under the current tree which have the **.txt** extension 


<br>

* python version: `python3 --version`

































## Windows Terminal Commands

* `cd` / `cd ..` / `dir`

* clear terminal: `cls`

* create folder/directory : `mkdir "directory name"`

* cut and paste file `move "doc.txt" C:\path`

* delete folder:
    * `rmdir ""`
    * `rmdir ""` /s (if it has files inside)

* delete file: `del /f "filename"`

* ip details: `ipconfig`

-----

### Sources

[1] https://www.linkedin.com/learning/python-essential-training-2018/

[2] https://medium.com/@saswat.sipun/shell-scripting-cheat-sheet-c0ecfb80391

[3] https://help.ubuntu.com/community/Beginners/BashScripting

[4] https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo