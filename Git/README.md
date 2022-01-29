# Git

Version control with git.

Contents
=======================

* [Documentation](#documentation)
* [Cheatsheets](#cheatsheets)    
* [Windows](#windows)
    * [Install & Update Git on Windows](#install--update-git-on-windows)
* [Linux](#linux)
    * [Install & Update Git on Linux](#install--update-git-on-linux)
* [Set Up & Configuration](#set-up--configuration)
* [Check Git Status](#check-git-status)

------

# Documentation

* [Git doc](https://git-scm.com/)
* [Hello Git - Github](https://docs.github.com/en/get-started/quickstart/hello-world)
* [Introduction to GitHub in Visual Studio Code](https://docs.microsoft.com/en-us/learn/modules/introduction-to-github-visual-studio-code/)

-------

# Cheatsheets

* [50 Git Commands You Should Know - by Fabio Pacific via freecodecamp](https://www.freecodecamp.org/news/git-cheat-sheet/?fbclid=IwAR3LGtnWpYV6xbM0yUKFVfFcfWIrEDJraf9h51ACtO4VmTEejz1nS-NTJsM)

------

# Windows
## Install & Update Git on Windows
* [Install Git on Windows](https://www.atlassian.com/git/tutorials/install-git#windows)

* **Update via Git Bash**: 
    * `git clone https://github.com/git/git`
    * windows: `git update-git-for-windows`

------

# Linux
## Install & Update Git on Linux

* [Install Git on Linux](https://www.atlassian.com/git/tutorials/install-git#linux)

* **Update**:
    * `sudo apt-get update`
    * `sudo apt-get install git`

------

# Set Up & Configuration

    git config --list
    git config --global user.name "name"
    git config --global user.email "email"

------

# Check Git Status

* `git log`: git history of current branch
* `git log --oneline --graph`
* `git status`: displays staged changes, unstaged changes and untracked files on working tree


------