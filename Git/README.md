# Git

Version control with git.

Contents
=======================

* Useful Links
    * [Hello Git - Github](https://docs.github.com/en/get-started/quickstart/set-up-git)
* [Windows](#windows)
    * [Install & Update Git on Windows](#install--update-git-on-windows)
* [Linux](#linux)
    * [Install & Update Git on Linux](#install--update-git-on-linux)
* [Set Up & Configuration](#set-up--configuration)
* [Check Git Status](#check-git-status)

------

# Windows
## Install & Update Git on Windows
* [Install](https://www.atlassian.com/git/tutorials/install-git#windows)

* **Update via Git Bash**: 
    * `git clone https://github.com/git/git`
    * windows: `git update-git-for-windows`

------

# Linux
## Install & Update Git on Linux

* [Install Git](https://www.atlassian.com/git/tutorials/install-git#linux)

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

