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
* [Fork & Pull Request](#fork--pull-request)

------

# Documentation

* [Git doc](https://git-scm.com/)
* [Hello Git - Github](https://docs.github.com/en/get-started/quickstart/hello-world)
* [Introduction to GitHub in Visual Studio Code](https://docs.microsoft.com/en-us/learn/modules/introduction-to-github-visual-studio-code/)

-------

# Cheatsheets

* [Basic git commands](https://www.dropbox.com/s/ubyvjp84cq42m5r/Git%20Cheat%20Sheet%20-%20Google%20Docs.pdf?dl=0)
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

    git config --list (or: git config -l)
    git config --global user.name "name"
    git config --global user.email "email"

------

# Check Git Status

* `git log`: git history of current branch
* `git log --oneline --graph`
* `git status`: displays staged changes, unstaged changes and untracked files on working tree

------

# Fork & Pull Request

* Fork the repo 
    * fork the repo from the owner's github repo page. This will automatically create a forked repo on your personal github
* Clone the forked repo (i.e. now being at your personal github) so that you can apply the desired changes. One way you can do that is:
    * grab the clone url: forked repo page > "Code" > "HTTPS" > copy the URL which ends with '.git'
    * in VS code: source control > clone > enter the URL > create workspace folder. Now you have a forked repo at your system
        * now you can apply the changes in the code. Commit the changes and push (these, as expected, will be applied in your forked repo)
* Submit a pull request to the project owner      
    * navigate to the forked repo on github > new pull request > create a new pull request
        * you can verify that by visiting the pull requests section of the original associated project

**Refresh changes from the remote (original) repository**

Let's suppose you have already forked a repo, and then submitted a pull request. What if you want to submit another pull request at a later time point? By that time, the remote repo might have changed, and those changes would not have been applied to your forked repo which would be outdated. Hence, in order to refresh those changes before you submit a new pull request use `git fetch`

* [Getting changes from a remote repository](https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository)
