# Contents

* [Shell Scripting](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#shell-scripting)
    * [Bash](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#bash)
        * [Commands](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#commands)
        * [Hashbang](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#hashbang)
* [Terminal - General](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#terminal---general)
    * [Bash Commands (Linux - MacOS - WSL)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#bash-commands-linux---macos---wsl)
        * [General](#general)
        * [Open](#open)
        * [Directories](#directories)
        * [Files](#file)
        * [Find](#find)
        * [Compression](#compression)
        * [Hard vs Soft (Symbolic) Copy](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#hard-vs-soft-symbolic-copy)
        * [Alias](#alias)
        * [cat | less | tail](#cat--less--tail)
        * [wc](#wc)
        * [grep](#grep)
        * [diff](#diff)
        * [echo](#echo)
        * [chmod](#chmod)
        * [xargs](#xargs)


        * [Miscellaneous](#miscellaneous)


        
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

Always use `man <command>` or `tldr <command>` for more information and options about the respective commands you want to use.

### General

* updates: `sudo apt-get update` | `sudo apt-get upgrade`

* `reboot` / `shutdown now` / `systemctl suspend` (like "sleep" on Windows)/ `systemctl hibernate`

* Ubuntu version: `df-h` `lsb_release -a` 

* Python version: `python3 --version`

* `cd` / `cd ..` 

* `ls`
    * display all folders and subfolders and files in a tree diagram: `tree <dirname>` (first install `sudo apt install tree`)
    * recursive output: `ls -R`

* the **manual page** of a command and guidance info for commands: `man <command>` e.g.: `$ man ls`
    * **quick guidance information** for commands: `tldr <command>`, e.g.: `$ tldr ls`


* locate where you are: `pwd`

* clear terminal: `clear` 
    * `clear -x` (clear the screen but keep terminal's scrollback buffer)

* history of terminal commands used: `history` `history 20`
    * search for the history of specific commands: `history | grep <command>` e.g. `history | grep git`
    * clear all history: `history -c`

* disc space / hard drive: `ncdu`
    * navigate via the arrows, you can also press enter and see the space allocated inside sub-directories
    * press `q` for exit

* ip details `nmcli device show`

-------

### Open

* **open** file/directory/application: `open <file_name>` `open <dir_name>` `open <app_name>` (this is likely to work only on macOS, for linux use `xdg-open <filename>`)

----

### Directories

* create directory (folder): `mkdir "dirname"`
    * create two folders in one command: `mkdir <dir1> <dir2>` 
    * create folder and nested subfolders: `mkdir -p <main_folder>/<subfolder>`

* delete/remove directory
    * if dir is empty: `rmdir <dirname>` / `rmdir <dir1> <dir2>`
    * if dir is not empty: `rm -rf <non_empty_folder>` / `rm -rf <non_empty_folder> <another_non_empty_folder>`

* copy a directory: `cp -r <dir_to_be_copied> <renamed_copied_and_pasted_dir>`

-----

### File

* create file: `touch <filename>`

* copy a file: `cp <file_to_be_copied> <renamed_copied_and_pasted_file>`

* move file (like cut and paste): `mv <file_to_be_moved> <dir_destination>`

* delete/remove file: `rm <filename>` `rm <file1> <file2>` 

* open file: `xdg-open <filename>`

------

### Find

* find **files** based on extension: `find . -name '*.txt'` ==> It finds all the files under the current tree which have the **.txt** extension 

* find **files** that exist in many directories: `find folder1 folder2 -name <file_name>`
    * use 'iname' for case-insensitive search: `find folder1 folder2 -iname <file_name>` 

* find **directories** under current tree matching the searched directory: `find . -type d -name <dir_name>`
    * `type -f` for files
    * `type-l` for symbolic (soft) links

* find **directories** under current tree matching a name: `find . -type d -name <dirname>`

----


### Compression

**tar vs zip vs gz (gzip)**

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

* you will probably use hard copies barely

**Creating a hard copy**

`ln <original> <link>`, e.g. `ln vehicles.txt cars.txt` ==> Content will be updated for both. If origin file is deleted and you do `$ cat cars.txt`, the link will still contain the original file

<br>

**Creating a soft link**

`ln -s <original> <link>`, e.g. `ln -s vehicles.txt cars.txt`  ==> link will have the '@' ==> if original file is deleted and you do `$ cat cars.txt`, the soft link will be broken (it will give 'No such file or directory')

-----

### Alias

you can use your own command (alias) replacing one of the official UNIX commands. E.g. `ls -ltr` displays a long format list of all files, sorted by modification date (oldest first). Let's say we want to create an alias called "my_alias" instead of typing "ls -ltr" => then `alias my_alias="ls -ltr"`

-----

### cat | less | tail

**cat**

* it prints a file's content
* you can also concatenate the content of multiple files into one file
* cat command can often be used in combination with the pipe operator "|" to feed a file's content as input to another command: `cat file1 | anothercommand`.

<br>

* print content of a file: `cat <filename>` | `cat <file1> <file2>`

* concatenate: `cat file1 file2 > file3`, e.g.  `cat a.txt b.txt > c.txt` => c.txt will have the content of "a" and "b"

Use `man cat` or `tldr cat` for more options

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

### wc

* e.g. count number of lines in file: `wc -l <filename>`

* count lines, words, and characters (bytes), e.g. `ls -all | wc` => will give output of lines words, and bytes

* man or tldr for more

-----

### grep

It stands for "*global regular expression print*"

* e.g. `grep ok file1.txt` will print the word "ok" as many times it is found on "file1" (otherwise it will not print anything)

### diff

It compares files and shows the difference in the content

* E.g. `diff -y <file1> <file2>` will dipslay the differences side by side

### echo
* print something to terminal: `echo "hello world!"`

* print a range of number, e.g.: `echo {1..5}`   

* create some content and insert it into a file, e.g.: `echo "I will put this text to a file >> <filename.txt>`

* `echo $(ls)` == `ls`
    * `echo "$(ls)"` (vertical output)

* `echo *` == `ls`

* display all files that start with some letter: `echo <letter>*`

* print path variable with a message: `echo "The path variable is: $PATH`

* print home path: `echo ~`

-------

### chmod

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
* `chmod a+r <filename>` means that [a]ll can now [r]ead 
*  `chmod og-r <filename>` means that you removed (-) the [r]ead permission from [o]thers and [g]roup

-----------

### xargs


Execute a command with piped *arguments* coming from another command, file, etc


Let's say we have multiple files we want to delete. On some cases it might be more convenient to e.g. display the file names into one file, and then invoke that file that will delete all other files. 

Let's say we have a txt file called "to_delete.txt" with two lines written: 1st line "file1.txt" and 2nd line "file2.txt". Let's suppose unter current tree we have 2 txt files called "file1.txt" and "file2.txt"

Then, via `cat to_delete.txt | xargs rm` we can remove all the files that are called via the "to_delete.txt", which in this case were file1.txt and file2.txt
    * if you `cat to_delete.txt | xargs -p rm` then will also be asked from the shell if you indeed want to remove those files!











































----------

### Miscellaneous

Various useful commands:

* `sort` ([examples](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-sort-command))
* `uniq` ([has to do with output](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-uniq-command))

----------------

Interrelated with the [chmod](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell_scripting#chmod) command:
* `chown` ([change user and group ownership of files and directories](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-chown-command))
* `unmask` ([control/modify default file permissions](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-umask-command))

-----------------

**Disk** usage:

* disk usage analyzer: `ncdu`
* [estimate and summarize file and dir space usage](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-du-command): `du`
    * e.g. `du -h <dirname>`
        *  `du -h <dirname> | sort -nr` 
* [overview of the filesystem disk space usage](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-df-command): `df` 
    *  `df -h` human readable form

---------

Interrelated with **paths**:

* `basename` | `dirname`

--------------

**Running processes**:

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

[Handle processes on remote machines and make a command run even after you log out or close the session to a server](https://www.freecodecamp.org/news/the-linux-commands-handbook/?fbclid=IwAR0cqzksTg5lzwxMcjMTagSlSd0E0IUNj7KznpVxf1GsJr2kenys52Eaemo#the-linux-nohup-command):

Allows for a process to live when the terminal gets killed: `nohup`
    * usage: `nohup <command>`




-------------------------

**Various**
 
* logging info: `who` `whoami`

* editors: `vi` / `vim`, `emacs`
    * `nano`


* users/account/passwords: `su` `sudo` | `passwd`



* networks / packets: `ping`, `traceroute`










































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

[7] https://unix.stackexchange.com/questions/57013/zip-all-files-in-directory

[8] https://stackoverflow.com/questions/20762094/how-are-zlib-gzip-and-zip-related-what-do-they-have-in-common-and-how-are-they#answer-20765054

[9] https://itsfoss.com/tar-vs-zip-vs-gz/

[10] https://superuser.com/questions/146754/on-linux-unix-does-tar-gz-versus-zip-matter#answer-1257441

[11] https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip#:~:text=1%20Answer&text=tar%20in%20itself%20just%20bundles,zip%20applies%20compression%20as%20well.&text=A%20zip%20archive%20is%20a,collection%20(of%20uncompressed%20files).#answer-10540952