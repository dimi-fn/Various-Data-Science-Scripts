# Contents

* [Shell Scripting](#shell-scripting)
    * [Bash](#bash)
        * [Commands]#commands)
        * [Hashbang](#hashbang)
* [Bash Commands (Linux - MacOS - WSL)](#bash-commands-linux---macos---wsl)
    * [Intro](#intro)
    * [General](#general)
    * [Open](#open)
    * [Directories](#directories)
    * [Files](#file)
    * [Compression](#compression)
        * [tar vs. zip vs. gz (gzip)](#tar-vs-zip-vs-gz-gzip)
    * [Hard vs Soft (Symbolic) Copy](#hard-vs-soft-symbolic-copy)
    * [$ alias](#-alias)
    * [$ cat | less | tail](#-cat--less--tail)
    * [$ wc](#-wc)
    * [$ find](#-find)
    * [$ grep | locate](#-grep--locate)
    * [$ diff](#-diff)
    * [$ echo | printf](#-echo--printf)
    * [$ chmod | chown | unmask](#-chmod--chown--unmask)
    * [$ xargs](#-xargs)
    * [$ env](#-env)
    * [Miscellaneous](#miscellaneous)
        * [Disk Usage](#disk-usage)
        * [Paths](#paths)
        * [Running Processes](#running-processes)
        * [Editors](#editors)
        * [logs/ users/ accounts/ passwords/ networks/ packets](#logs-users-accounts-passwords-networks-packets)
        * [Remote Connection](#remote-connection)
        * [Various](#various)
* [Windows Terminal - Commands](#windows-terminal---commands)
    * [Search Paths - Files](#search-paths---files)
    * [find](#find-windows)
* [To Further Explore](#to-further-explore)
* [Encryption](#encryption)
    * [Linux](#linux)
    * [Windows](#windows)

----

# Shell Scripting

`Shell scripting` is a program to run on UNIX shell, and `Bash` (Bourne Again SHell) is a Unix shell and interactive command line language and interpreter. It refers to the whole shell, and it is the default shell on Linux and Mac OS.

* The terminal can be used on Linux and Mac, the git bash on Windows

## Bash 
### Commands

* `which bash` : to know where is your bash ==> this will be the first line of code in the script after `#!`
    * e.g. if after typing "which bash" the result is "/bin/bash" then the 1st line of code should be: `#!/bin/bash`
    * in case permission is required: `chmod +x 'bash_script'.sh`

* terminal (in order to run the .sh file):
    1) go the path of the bash script (where the filename`.sh` is located)
    2) `chmod +x filename.sh`
    3) `./filename.sh`   

Or just `$ bash filename.sh`

* no spaces among code, it is like typing in the terminal

* `-eq` : To check if two numbers are equal

* `-ne` : To check if two number are not equal

* `-gt` : To check if num1 > num2

* `-lt` : To check if num1 < num2

* `-le` : less than equal to

### Hashbang 

Scripts start with an interpretive directive which is called the "**Hashbang**" or "**Shebang**"

* `#!` ==> ("hash" + "bang" ==> the hashbang (or shebang)) 
* /bin/bash ==> the path to the Bash executable
    * `#!/bin/bash` altogether

The above will tell the shell that this is a Bash script, and that it should be run as such.

----

* `#!/usr/bin/env/ python3` 

* `usr/bin/env python3` --> the path to the executable that will run the script along with any other optional arguments

    * it is a common pattern for Unix based systems

    * it allows a script to be invoked from the command line

    * it should be in the very first line of the script

    * on Windows this line will be considered a comment and hence will be completely ignored
    * on linux of course it will not be ignored since it is Unix based, same on Mac because it is based on the BSD Unix

# Bash Commands (Linux - MacOS - WSL)

## Intro

Always use `man <command>` or `tldr <command>` for more information and options about the respective commands you want to use.
* `q` for exit | `h` for displaying the reference
* `Ctrl+C` to stop indefinite executions, e.g. while using ping


| Arguments | Description |
|------|------|
|  `.` | currently directory (e.g., ./my_project) |
|  `..` | one folder up (cd .. (1 directory back), ../../my_project => this will move up 2 directories)  |
| `/` | root of system| 
| `~` | home directory (usually the path: /users/username). It moves back to folders with regard to this path by including it at the start of your path, e.g., ~/my_project|


## General

* updates: `sudo apt-get update` | `sudo apt-get upgrade`
    * enable the firewall: `sudo ufw enable`

* `reboot` / `shutdown now` / `systemctl suspend` (like "sleep" on Windows)/ `systemctl hibernate`

* Ubuntu version: `lsb_release -a`

* Python version: `python3 --version`

* `cd` / `cd ..` 

* `ls`
    * display all folders and subfolders and files in a tree diagram: `tree <dirname>` (first install `sudo apt install tree`)
    * show also hidden files (e.g. the .git file): `ls -a`
    * recursive output: `ls -R`
    * output with permissions and file types:
        * `ls -l`
        * `ls -l <directory>`

* the **manual page** of a command and guidance info for commands: `man <command>` e.g.: `$ man ls`
    * **quick guidance information** for commands: `tldr <command>`, e.g.: `$ tldr ls`


* locate where your current path is: `pwd`
    * go to home directory: `cd` | `cd ~` | `cd /home/<user>`

* clear terminal: `clear` | `cntl + l`
    * `clear -x` (clear the screen but keep terminal's scrollback buffer)

* history of terminal commands used: `history` `history 20`
    * search for the history of specific commands: `history | grep <command>` e.g. `history | grep git`
    * clear all history: `history -c`

* disc space / hard drive: `ncdu`
    * navigate via the arrows, you can also press enter and see the space allocated inside sub-directories
    * press `q` for exit
    * [more here](#disk-usage)

* machine and OS info: `uname`    

* ip details `nmcli device show`

-------

## Open

* **open** file/directory/application: `open <file_name>` `open <dir_name>` `open <app_name>` (this is likely to work only on macOS, for linux use `xdg-open <filename>`)

----

## Directories

* create directory (folder): `mkdir "dirname"`
    * create two folders in one command: `mkdir <dir1> <dir2>` 
    * create folder and nested subfolders: `mkdir -p <main_folder>/<subfolder>`

* delete/remove directory
    * if dir is empty: `rmdir <dirname>` / `rmdir <dir1> <dir2>`
    * if dir is not empty: `rm -rf <non_empty_folder>` / `rm -rf <non_empty_folder> <another_non_empty_folder>`

* copy a directory: `cp -r <dir_to_be_copied> <renamed_copied_and_pasted_dir>`

-----

## File

* create file: `touch <filename>` | `touch {file1,file2,file3}.txt` (brace expansion without spaces) | for many files: `touch {1..100}.txt` => will create 100 txt files

* copy a file: `cp <file_to_be_copied> <renamed_copied_and_pasted_file>`

* move file (like cut and paste): `mv <file_to_be_moved> <dir_destination>`

* delete/remove file: `rm <filename>` `rm <file1> <file2>` 
    * remove everything under current tree: `rm *`

* open file: `xdg-open <filename>`

----

## Compression

### tar vs. zip vs. gz (gzip)

* [tar == uncompressed archive file](https://itsfoss.com/tar-vs-zip-vs-gz/)
* [.zip == (usually) compressed archive file](https://itsfoss.com/tar-vs-zip-vs-gz/)
* [.gz == file (archive or not) compressed using gzip](https://itsfoss.com/tar-vs-zip-vs-gz/)

-----

* [.zip is an archive format using, usually, the Deflate compression method. The .gz gzip format is for single files, also using the Deflate compression method. Often gzip is used in combination with tar to make a compressed archive format, .tar.gz. The zlib library provides Deflate compression and decompression code for use by zip, gzip, png (which uses the zlib wrapper on deflate data), and many other applications.](https://stackoverflow.com/questions/20762094/how-are-zlib-gzip-and-zip-related-what-do-they-have-in-common-and-how-are-they#answer-20765054)

------

So, essentially it is about **tar.gz vs. zip**:

**tar.gz**:

* [Stores unix file attributes: uid, gid, permissions (most notably executable). The default may depend on your distribution, and can be toggled with options.](https://superuser.com/questions/146754/on-linux-unix-does-tar-gz-versus-zip-matter#answer-1257441)
* [Consolidates all files to be archived in one file ("Tape ARchive").](https://superuser.com/questions/146754/on-linux-unix-does-tar-gz-versus-zip-matter#answer-1257441)
* [Actual compression is done by GZIP, on the one .tar file](https://superuser.com/questions/146754/on-linux-unix-does-tar-gz-versus-zip-matter#answer-1257441)

**zip**

* [Stores MSDOS attributes. (Archive, Readonly, Hidden, System)](https://superuser.com/questions/146754/on-linux-unix-does-tar-gz-versus-zip-matter#answer-1257441)
* [Compresses each file individually, then consolidates the individually compressed files in one file](https://superuser.com/questions/146754/on-linux-unix-does-tar-gz-versus-zip-matter#answer-1257441)
* [Includes a file table at the end of the file](https://superuser.com/questions/146754/on-linux-unix-does-tar-gz-versus-zip-matter#answer-1257441) 

------

* [tar in itself just bundles files together (the result is called a tarball), while zip applies compression as well.](https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip#:~:text=1%20Answer&text=tar%20in%20itself%20just%20bundles,zip%20applies%20compression%20as%20well.&text=A%20zip%20archive%20is%20a,collection%20(of%20uncompressed%20files).#answer-10540952)

* ====> !!!!! [Usually you use gzip along with tar to compress the resulting tarball, thus achieving similar results as with zip.](https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip#:~:text=1%20Answer&text=tar%20in%20itself%20just%20bundles,zip%20applies%20compression%20as%20well.&text=A%20zip%20archive%20is%20a,collection%20(of%20uncompressed%20files).#answer-10540952)

[For reasonably large archives there are important differences though. A zip archive is a collection of compressed files. A gzipped tar is a compressed collection (of uncompressed files). Thus a zip archive is a randomly accessible list of concatenated compressed items, and a .tar.gz is an archive that must be fully expanded before the catalog is accessible.](https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip#:~:text=1%20Answer&text=tar%20in%20itself%20just%20bundles,zip%20applies%20compression%20as%20well.&text=A%20zip%20archive%20is%20a,collection%20(of%20uncompressed%20files).#answer-10540952)

* [The caveat of a zip is that you don't get compression across files (because each file is compressed independent of the others in the archive, the compression cannot take advantage of similarities among the contents of different files); the advantage is that you can access any of the files contained within by looking at only a specific (target file dependent) section of the archive (as the "catalog" of the collection is separate from the collection itself).](https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip#:~:text=1%20Answer&text=tar%20in%20itself%20just%20bundles,zip%20applies%20compression%20as%20well.&text=A%20zip%20archive%20is%20a,collection%20(of%20uncompressed%20files).#answer-10540952)

* [The caveat of a .tar.gz is that you must decompress the whole archive to access files contained therein (as the files are within the tarball); the advantage is that the compression can take advantage of similarities among the files (as it compresses the whole tarball).](https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip#:~:text=1%20Answer&text=tar%20in%20itself%20just%20bundles,zip%20applies%20compression%20as%20well.&text=A%20zip%20archive%20is%20a,collection%20(of%20uncompressed%20files).#answer-10540952)

-----

* **tar**: create an archive from files: `tar cf <choosename.tar> <file1> <file2>`

* **zip** compress dir and its contents [r]ecursively: `zip -r <filename.zip> <dirname_tobe_zipped>`

* **gzip**: compress a file specifying the output filename: 
`gzip -c <file_tobe_compressed> > <choosename>.gz`
    * so, after creating a `tar` file, then apply `gzip` to compress
        * e.g. `tar cf foo.tar <file1> <file2>` => and then => `gzip -c foo.tar > foo.gz`

* `gunzip` ==> equivalent to `gzip -d`

------

## Hard vs Soft (Symbolic) Copy

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

* you will probably use hard copies barely

**Creating a hard copy**

`ln <original> <link>`, e.g. `ln vehicles.txt cars.txt` ==> Content will be updated for both. If origin file is deleted and you do `$ cat cars.txt`, the link will still contain the original file

<br>

**Creating a soft link**

`ln -s <original> <link>`, e.g. `ln -s vehicles.txt cars.txt`  ==> link will have the '@' ==> if original file is deleted and you do `$ cat cars.txt`, the soft link will be broken (it will give 'No such file or directory')

-----

## $ alias

you can use your own command (alias) replacing one of the official UNIX commands. E.g. `ls -ltr` displays a long format list of all files, sorted by modification date (oldest first). Let's say we want to create an alias called "my_alias" instead of typing "ls -ltr" => then `alias my_alias="ls -ltr"`

-----

### $ cat | less | tail

**cat**

* it prints a file's content (*it makes only sense for txt files, not binary like images*)
* you can also concatenate the content of multiple files into one file
* cat command can often be used in combination with the pipe operator "|" to feed a file's content as input to another command: `cat file1 | anothercommand`.

<br>

* print content of a file: `cat <filename>` | `cat <file1> <file2>`

* concatenate: `cat file1 file2 > file3`, e.g.  `cat a.txt b.txt > c.txt` => c.txt will have the content of "a" and "b"

<br>

* you can also use `more <txtfile>` and read the content more easily by pressing space bar for navigation through the content.

----

**less**

* it prints the content of file in an interactive UI way

`less <filename>`

* man or tldr for more

-----

**tail**

e.g. print last 2 lines of a file: `tail -n 2 <filename>`

* man or tldr for more

-----

## $ wc

* e.g. count number of lines in file: `wc -l <filename>`

* number of files: `ls -1 | wc -l`

* count lines, words, and characters (bytes), e.g. `ls -all | wc` => will give output of lines words, and bytes

* man or tldr for more

------

## $ find

* find **files** based on extension: `find . -name '*.txt'` ==> It finds all the files under the current tree which have the **.txt** extension 

* find **files** that exist in many directories: `find folder1 folder2 -name <file_name>`
    * use 'iname' for case-insensitive search: `find folder1 folder2 -iname <file_name>` 

* `find /home/ -name some_text.txt `: find file named "some_text.txt" within the home directory and its subdirectories

* find **directories** under current tree matching the searched directory: `find . -type d -name <dir_name>`
    * `type -f` for files
    * `type-l` for symbolic (soft) links

* find **directories** under current tree matching a name: `find . -type d -name <dirname>`

------

## $ grep | locate

**greb**: It stands for "*global regular expression print*"

* e.g. `grep "ok" file1.txt` will print the word "ok" as many times it is found on "file1" (otherwise it will not print anything)

* `ping google.com`
    * run only 2 times: `ping -c 2 google.com`
        * grap content containing "bytes from": `ping -c 2 google.com | grep "bytes from"`
            * cut content, search for the [4]th [f]ield based on the "=" [d]elimeter to slice up lines based on that particular criteria `ping -c 2 google.com | grep "bytes from" | cut -d = -f 4` => this will give only the response time!

<br>

**locate**: `locate -i analysis*analyst` ==> will search for any file that contains the word "analysis" and "analyst" (the "-i" makes the search case-insensitive).

## $ diff

It compares files and shows the difference in the content

* E.g. `diff -y <file1> <file2>` will dipslay the differences side by side

## $ echo | printf
* print something to terminal: `echo "hello world!"`

* print a range of number, e.g.: `echo {1..5}`   

* create some content and insert it into a file, e.g.: `echo "I will put this text to a file >> <filename.txt>`

* `printf "1\n2\n3"` <--> this will not work with echo as desired

* `echo $(ls)` == `ls`
    * `echo "$(ls)"` (vertical output)

* `echo *` == `ls`

* display all files that start with some letter: `echo <letter>*`

* print path variable with a message: `echo "The path variable is: $PATH`

* print home path: `echo ~`

-------

## $ chmod | chown | unmask

<ins>It is used to access and change the permissions of a file or directory<ins>

Take the ouput of  `ls -al` and see the output.

* In Unix, every file has **read** (`r`), **write** (`w`), and **execute** (`x`) 
permissions
    * `-`: normal file
    * `d`: dir
    * `l`: link

Noticing the output of `ls -al` you can see 3 sets of values:
* 1st set: permissions of the owner
* 2nd set: permissions of the members of the group that the file is associated with
* 3rd set: permissions of everyone else

E.g.: `rwx` means read-write-execute persmission

<br>

chmod followed by a space and a letter:
* `a`: all
* `u`: user
* `g`: group
* `o`: others

Then by `+` or `-` you can add or remove a permission

E.g. 
* `chown this_user some_text.txt will make "this_user" the owner of "some_text.txt"`
* `chmod a+r <filename>` means that [a]ll can now [r]ead 
*  `chmod og-r <filename>` means that you removed (-) the [r]ead permission from [o]thers and [g]roup

-----------

Interrelated with the [chmod](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#chmod) command:
* `chown` ([change user and group ownership of files and directories](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-chown-command))
* `unmask` ([control/modify default file permissions](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-umask-command))

-------------

## $ xargs

Execute a command with piped *arguments* coming from another command, file, etc


Let's say we have multiple files we want to delete. On some cases it might be more convenient to e.g. display the file names into one file, and then invoke that file that will delete all other files. 

Let's say we have a txt file called "to_delete.txt" with two lines written: 1st line "file1.txt" and 2nd line "file2.txt". Let's suppose unter current tree we have 2 txt files called "file1.txt" and "file2.txt"

Then, via `cat to_delete.txt | xargs rm` we can remove all the files that are called via the "to_delete.txt", which in this case were file1.txt and file2.txt
    * if you `cat to_delete.txt | xargs -p rm` then will also be asked from the shell if you indeed want to remove those files!

## $ env

* show the environment: `env`

Usage: [The env command can be used to pass environment variables without setting them on the outer environment (the current shell). Suppose you want to run a Node.js app and set the "USER" variable to it.](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-env-command). Then you can:

env USER=<your_username> node app.js


[and the USER environment variable will be accessible from the Node.js app via the Node process.env interface.](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-env-command
)

<br>

* Alse see `printenv`

--------------

## Miscellaneous

### Disk Usage

* disk usage analyzer: `ncdu`
* [estimate and summarize file and dir space usage](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-du-command): `du`
    * e.g. `du -h <dirname>`
        *  `du -h <dirname> | sort -nr` 
* [overview of the filesystem disk space usage](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-df-command): `df` 
    *  `df -h` human readable form

* `top`: similar to task manager in Windows

--------------

### Paths

* `basename` | `dirname`

--------------

### Running Processes

| Information/State | Description |
|----|----|
| **PID** | Process Id |
| **TT** | Terminal Id is used |
| **STAT** | State of process |
|`I`| idle (sleeping for longer than 20 sec.)|
|`R`| runnable process|
|`S`| sleeping for less than 20 sec.|
|`T`| a stopped process|
|`U`| a process in uninterruptible wait|
|`R`| runnable process|
|`R`| runnable process|
|`Z`| a zombie: a dead process|
|**+**| process is in the foreground|
|**s**| process is a session leader|

<br>

* `ps`
    * e.g.: `ps auxww` will list all running processes including the full commanding string
        * you can do it for specific applications, e.g.: `ps axww | grep "Visual Studio Code"`

* display dynamic real-time informartion about running processes: `top` 
    * `htop`

* `kill`
    * `kill <PID>`
* `killall`     
    * `killall <name>` 

* display status of jobs in current session: `jobs`
* resume jobs that have been suspended: `bg`
* run jobs in foreground: `fg`

<br>

* display the kind of command the shell will execute: `type`

* locate a program in the user's path: `which`



<br>

* [Handle processes on remote machines and make a command run even after you log out or close the session to a server](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-nohup-command):

Allows for a process to live when the terminal gets killed: `nohup`
* usage: `nohup <command>`

<br>

`crontab`: [Cron jobs are jobs that are scheduled to run at specific intervals. They can be used on servers to perform maintenance and automations](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-crontab-command)


-------------

### Editors

* `vi` / `vim`, `emacs`
    * `nano`

------

### logs/ users/ accounts/ passwords/ networks/ packets

* logging info: `who` `whoami`

* users/account/passwords: `su` | `sudo` | `passwd`

* networks / packets: `ping` | `traceroute`

----------------

### Remote Connection

Log in remotely to another linux machine, e.g.: `ssh user_name@104.25.111.22` will login to 104.25.111.22 with the username "user_name" 

----------------

### Various

* `sort` ([examples](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-sort-command))
* `uniq` ([has to do with output](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-uniq-command))

* which / whereis
    * whereis, additionaly to "which", will give you the path to the binary, the path to the libraries, and the path for "man" page of the respective program you are searching for

* download files from the web: `wget`

* calendar: `cal` | calculator: `bc`

------------

# Windows Terminal - Commands

* `help <command>`: like "man" command for linux

* `cd` / `cd ..` / `dir` / `tree <dirname>`
    * change drive directory: `cd /d <another drive>:`
    * or just `<another drive>:`

* clear terminal: `cls`

* create
    * folder/directory : `mkdir "directory name"`
    * file: be at the path you want to create it, otherwise specify the path `type nul > filename.txt`
        * write some text to the .txt file: `echo enter your text here > filename.txt`

* copy file to another path: `copy <fileName>` <to_pathDirectory>`

* cut and paste file `move "doc.txt" C:\path`

* delete folder:
    * `rmdir ""`
    * `rmdir ""` /s (if it has files inside)

* delete file: `del /f "filename"`

* ip details: `ipconfig`

* access network path by creative a map drive
    * `pushd <path>`
    * to delete mapped drives: first navigate to any other drive except the one to be deleted, then `net use /del <mappedDriveName>:`

## Search Paths - Files

* find the path of a file based on filename: `dir /s *foo*`, or based file extension: `dir /s *.txt`
    * /s lists every occurrence of the specified file name within the specified directory and all subdirectories.
        * `dir /b /s *foo*` to search under current directory tree

## $find (Windows)

* `find /i "python" C:\Users\*.txt` will search for all txt files containing the string "python" which are located in the Users directories and subdirectories

-------

# To Further Explore

* [LeCoupa/awesome-cheatsheets](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh)

* [Bash Reference Manual](https://tiswww.case.edu/php/chet/bash/bashref.html)

* [learnshell.org](https://www.learnshell.org/)

-------

# Encryption

* Public Key Infrastructure (PKI)
* Asymmetric cryptography: you create a **public** and a **private** key pair (2 keys)
    * `public` key can be given to others so that data can be *encrypted* by them (it is meant to be accessible)
    * `private` key is used so that you can *decrypt* that data (must be secret key)

* PGP (Pretty Good Privacy) Encryption 

## Linux

* GnuPG: [How to Encrypt and Decrypt Files With GPG on Linux](https://www.howtogeek.com/427982/how-to-encrypt-and-decrypt-files-with-gpg-on-linux/), [The Complete PGP Encryption Tutorial | Gpg4win & GnuPG](https://www.youtube.com/watch?v=CEADq-B8KtI&ab_channel=HackerSploit)
* GPA GNU privacy assistant -> graphical user interface that allows you to manage the public & private key pairs

        sudo apt-get install gnupg2 gpa


* generate key:
    * `gpg --full-generate-key` > select 1 (default for RSA and RSA) > type the maximum bits long for the RSA keysize > create passphrase
        * if problems occur with regard to the graphical UI: `sudo apt install libcanberra-gtk-module libcanberra-gtk3-module`

* `sudo gpa` to launch the GPA UI

* GPA UI
    * select "export keys" by right clicking, so that the PGP file containing the public key can be created (.asc file)
    * select back up for back up

* to encrypt someone else's file: GPA UI > keys > import keys > select the pgp file

* to encrypt your data: GPA UI > windows > clipboard
    * type your message to be encrypted > file > encrypt > select the public key (sign it if you want to) with regard to the key pair created earlier
    * to decrypt it: file > decrypt

*Note*: if gpa does not launch when sudo gpa via terminal, then launch it manually via the applications menu > gpa

## Windows

* [Gpg4win](https://www.gpg4win.org/), [download](https://www.gpg4win.org/get-gpg4win.html)
    * [Install](https://gpg4win.de/doc/en/gpg4win-compendium_11.html)
    * [Gpg4win Compendium](https://files.gpg4win.org/doc/gpg4win-compendium-en.pdf)

Encryption Process:

* Create a key pair:
    * kleopatra app/file/new key pair/create a personal OpenPGP key pair
        * advanced settings: select the maximum RSA value
        * use a passphrase
        * while the key is created, you can move randomly your mouse and/or write something using your keyboard for greater entropy 
            * in the kleopatra app interface in the "certificates" section: right click> export key -> this will create a .asc file containing the public key (`"BEGIN PGP PUBLIC KEY BLOCK ... END PGP PUBLIC KEY BLOCK`")
            * right click>export private key (so you can keep a back up)

* now you can start encypting data, but first you have to import the cerfificate based on the above key pair created:
    * kleopatra app interface/import certificate/select the .asc file containing the public key created above
        * now you can begin encrypting data. E.g., create a txt, copy the content, go to kleopatra app icon > clipboard> right click > encrypt > add recipient (select the one respecting the relative key pair)
            * now if you paste in another txt file you will see the message of type "`BEGIN PGP MESSAGE ... BEGIN PGP MESSAGE`"

* to decrypt that data:  
    * by default you have the PGP message already copied from previous step    
    * navigate again to kleopatra icon > right click > clipboard > decrypt > fill out the key pair passphrase: now if you paste somewhere you will see the encrypted message/content (note: if the PGP message is not copied from previous step, then the "decrypt" icon will remain grayed out and cannot be selected)         


**Encrypt files**:

[Encrypted files in Windows with GPG and Kleopatra](https://www.youtube.com/watch?v=QmE4LrBSChQ)

* create a key pair as shown above (kleopatra > file > new key pair)

* click "Signin/Encrypt" via kleopatra > choose the file to be encrypted > click "encrypt for me" and leave the rest unclicked > encrypt
    * a .gpg file has now been created. Double-click  and use passphrase to unlock

<b>

[Back up - Transfer your Keys](https://gpgtools.tenderapp.com/kb/gpg-keychain-faq/backup-or-transfer-your-keys)

--------

### Sources

[1] https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo

[2] https://medium.com/@saswat.sipun/shell-scripting-cheat-sheet-c0ecfb80391

[3] https://help.ubuntu.com/community/Beginners/BashScripting

[4] https://www.linkedin.com/learning/python-essential-training-2018/ 

[5] https://askubuntu.com/questions/432284/are-hard-links-equivalent-to-windows-shortcuts?newreg=bedfb396262d490d86f7fab8bd8fe0f2

[6] https://ostechnix.com/explaining-soft-link-and-hard-link-in-linux-with-examples/

[7] https://unix.stackexchange.com/questions/57013/zip-all-files-in-directory

[8] https://stackoverflow.com/questions/20762094/how-are-zlib-gzip-and-zip-related-what-do-they-have-in-common-and-how-are-they#answer-20765054

[9] https://itsfoss.com/tar-vs-zip-vs-gz/

[10] https://superuser.com/questions/146754/on-linux-unix-does-tar-gz-versus-zip-matter#answer-1257441

[11] https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip#:~:text=1%20Answer&text=tar%20in%20itself%20just%20bundles,zip%20applies%20compression%20as%20well.&text=A%20zip%20archive%20is%20a,collection%20(of%20uncompressed%20files).#answer-10540952

[12] https://www.linkedin.com/learning/learning-bash-scripting-2013/

[13] https://www.youtube.com/watch?v=s3ii48qYBxA&ab_channel=DistroTube

[14] https://www.freecodecamp.org/news/linux-command-line-bash-tutorial/

[15] https://www.freecodecamp.org/news/basic-linux-commands-bash-tips-you-should-know/

[16] https://wiki.ubuntu.com/BasicSecurity