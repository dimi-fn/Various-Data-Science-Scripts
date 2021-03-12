# Contents

* [Shell Scripting](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#shell-scripting)
    * [Bash](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#bash)
        * [Commands](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#commands)
        * [Hashbang](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#hashbang)
* [Terminal - General](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#terminal---general)
    * [Bash Commands (Linux - MacOS - WSL)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#bash-commands-linux---macos---wsl)
        * [Hard vs Soft (Symbolic) Copy](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#hard-vs-soft-symbolic-copy)
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


-------

* open file/directory/application `open <file_name>` `open <dir_name>` `open <app_name>`


-----


* create directory (folder): `mkdir "dirname"`
    * create two folders in one command: `mkdir <dir1> <dir2>` 
    * create folder and nested subfolders: `mkdir -p <main_folder>/<subfolder>`

* delete directory
    * if dir is empty: `rmdir <dirname>` / `rmdir <dir1> <dir2>`
    * if dir is not empty: `rm -rf <non_empty_folder>` / `rm -rf <non_empty_folder> <another_non_empty_folder>`

* copy a folder: `cp -r <folder_to_be_copied> <renamed_copied_and_pasted_folder>`: 


------

* create file: `touch <filename>`

* copy a file: `cp <file_to_be_copied> <renamed_copied_and_pasted_file>`

* move file (like cut and paste): `mv <file_to_be_moved> <dir_destination>`

* delete file: `rm <filename>`

* open file: `xdg-open <filename>`


------

**Find**:

* find **files** based on extension: `find . -name '*.txt'` ==> It finds all the files under the current tree which have the **.txt** extension 

* find **files** that exist in many directories: `find folder1 folder2 -name <file_name>`
    * use 'iname' for case-insensitive search: `find folder1 folder2 -iname <file_name>` 

* find **directories** under current tree matching the searched directory: `find . -type d -name <dir_name>`
    * `type -f` for files
    * `type-l` for symbolic (soft) links

* find **directories** under current tree matching a name: `find . -type d -name <dirname>`



-----

* python version: `python3 --version`

----


### Hard vs Soft (Symbolic) Copy

Files on Unix file systems are stored via `inodes`. An inode is a number that the filesystem  uses to *map* a file name to a particular location on the physical hard drive.


| **Hard Copy** | **Soft (Symbolic) Copy** |
| ------ | -------------------------- |
| mirror copy of the original file | actual link to the original file |
| if you delete the original file, the hard link will still  carry the data | if you delete the file, the soft link has no value because it points to a non-existent file |
| they are pointers to the same location of the disc | they work like shortcuts|
| it cannot cross the file system: it works only on the same filesystem, you cannot link to external filesystems (disks) | it can cross the file system|
| it allows to link to directories| cannot link directories|
| same inode number and permissions with those of original file| inode number and file permissions are different from the original file, hence permission will not be updated |
| it carries the actual contents of original file even if the original file is moved or removed| it carries only the path, not the contents of original file |

**Creating a hard copy**

`ln <original> <link>`, e.g. `ln vehicles.txt cars.txt` ==> Content will be updated for both. If origin file is deleted and you do `$ cat cars.txt`, the link will still contain the original file

<br>

**Creating a soft link**

`ln -s <original> <link>`, e.g. `ln -s vehicles.txt cars.txt`  ==> link will have the '@' ==> if original file is deleted and you do `$ cat cars.txt`, the soft link will be broken (it will give 'No such file or directory')





















-----

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

[1] https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo

[2] https://medium.com/@saswat.sipun/shell-scripting-cheat-sheet-c0ecfb80391

[3] https://help.ubuntu.com/community/Beginners/BashScripting

[4] https://www.linkedin.com/learning/python-essential-training-2018/ 

[5] https://askubuntu.com/questions/432284/are-hard-links-equivalent-to-windows-shortcuts?newreg=bedfb396262d490d86f7fab8bd8fe0f2

[6] https://ostechnix.com/explaining-soft-link-and-hard-link-in-linux-with-examples/