# Git & Github

Git is a free and open source version control system. 
* Git is the tool that tracks the changes in your code, GitHub is a website where you host all of your Git repositories online (remotely on the website's cloud)

Contents
=======================

* [Documentation](#documentation)
* [Cheatsheets](#cheatsheets)    
* [Windows](#windows)
    * [Install & Update Git on Windows](#install--update-git-on-windows)
* [Linux](#linux)
    * [Install & Update Git on Linux](#install--update-git-on-linux)
* [Set Up & Configuration](#set-up--configuration)
* [VS Code & Github](#vs-code--github)
    * [Publish to GitHub from VS Code](#publish-to-github-from-vs-code)
* [Git Commands](#git-commands)
* [Check Git Status](#check-git-status)
* [Fork & Pull Request](#fork--pull-request)

------

# Documentation

* [Git doc](https://git-scm.com/)
* [Hello Git - Github](https://docs.github.com/en/get-started/quickstart/hello-world)
* [Introduction to GitHub in Visual Studio Code](https://docs.microsoft.com/en-us/learn/modules/introduction-to-github-visual-studio-code/)

-------

# Cheatsheets

* [Git Cheatsheet by Github](https://training.github.com/downloads/github-git-cheat-sheet/)
* [50 Git Commands You Should Know - by Fabio Pacific via freecodecamp](https://www.freecodecamp.org/news/git-cheat-sheet/?fbclid=IwAR3LGtnWpYV6xbM0yUKFVfFcfWIrEDJraf9h51ACtO4VmTEejz1nS-NTJsM)

------

# Windows
## Install & Update Git on Windows
* [Install Git on Windows](https://www.atlassian.com/git/tutorials/install-git#windows)

* **Update via Git Bash**: 
    * `git clone https://github.com/git/git`
    * windows: `git update-git-for-windows`
    * check git version: `git --version`

------

# Linux
## Install & Update Git on Linux

Git is most likely installed by default on linux (and mac) OS.

* [Install Git on Linux](https://www.atlassian.com/git/tutorials/install-git#linux)

* **Update**:

    * https://git-scm.com/download/linux
    * https://unix.stackexchange.com/a/170831

<br>        

        sudo add-apt-repository ppa:git-core/ppa -y
        sudo apt-get update
        sudo apt-get install git -y
        git --version

------

# Set Up & Configuration

    git config --list (or: git config -l)
    git config --global user.name "name"
    git config --global user.email "email"

------

# VS Code & Github

* Make sure you have the latest version of VS Code: select the Profile/accounts icon in the activity bar, then select Check for Updates
* On VS Code, sign in with your github account via the account icon at the bottom of the activity bar
* Extensions: intall "Github Pull Requests and Issues"
* VScode: click on the 'Accounts' gear, from there you can turn on the github sync settings if you want to

## Publish to GitHub from VS Code

The are three ways to do that:

1st way: 
* Github: Create your repo on github and copy the repo HTTPS URL 
* VS Code: source control > open folder (to create a workspace directory) > (git bash, by being under your project directory:) git clone 'the_HTTPS_URL' > 'git add' or 'git add .' > 'git commit -m "your commit message"' > git push

2nd way (similar to the 1st way but without the terminal):
* source control > open folder (to create a workspace directory) > (via source control) clone repository > paste the HTTPS repo URL > commit any changes through the CLI of VS Code and then push via the button in the bottom

3rd way (integrate all steps above into one via VSCode - it prerequires that you have already linked your GitHub on VS Code): 
    * VS Code: source control > open foler (to create a workspace directory) > 'new file' to add e.g. your README.md file > (source control:) publish to Github (there's no need to initialize the repo on GitHub, since this will automatically be created there)

------

**Additional**:

* `.env.development`: Before you pubish to github (and after you have created a repo), you might need to create a .env.development file. This file type is used to define program information that is confidential. Confidential information such as database connection strings should not be pushed to GitHub.

1. On the File menu, select New File
2. Add the following the file: `CONNECTION_STRING=secret-that-should-not-be-pushed-to-github`
3. On the File menu, select Save
4. Save the file as .env.development.

Next, when you are ready to publish on github, deselect the .env.development option from the selected files

* [How To Use GitHub with VS Code](https://www.youtube.com/watch?v=3Tn58KQvWtU&list=PLpPVLI0A0OkLBWbcctmGxxF6VHWSQw1hi&index=2&ab_channel=DevWorld)

------

# Git Commands

* `clone`: bring a repo that is hosted somewhere like github into a folder (directory) on your local machine
* `add`: track your files and changes in Git
* `commit`: save your files in Git
* `push`: upload Git commits remotely, e.g. on Github
* `pull`: download changes from a remote repo to your local machine, i.e. the opposite of "push"

------

# Check Git Status
* `git log`: git history of current branch (type "q" to exit)
* `git log --oneline --graph`
* `git status`: displays staged changes, unstaged changes and untracked files on working tree

------

# Fork & Pull Request
* `Fork the repo`
    * fork the repo from the owner's github repo page. This will automatically create a forked repo on your personal github
* `Clone the forked repo` (i.e. the remote repo now hosted on your personal github) so that you can apply the desired changes. One way you can do that is:
    * grab the clone url: forked repo page > "Code" > "HTTPS" > copy the URL which ends with '.git'
    * in VS code: source control > clone > enter the URL > create workspace folder. Now you have a forked repo at your system
        * now you can apply the changes in the code. Commit the changes and push (these, as expected, will be applied in your forked repo)
* `Submit pull request to the project owner`      
    * navigate to the forked repo on github > new pull request > create a new pull request
        * you can verify that by visiting the pull requests section of the original associated project

**Refresh changes from the remote (original) repository**

Let's suppose you have already forked a repo, and then submitted a pull request. What if you want to submit another pull request at a later time point? By that time, the remote repo might have changed, and those changes would not have been applied to your forked repo which would remain outdated. Hence, in order to refresh those changes before you submit a new pull request, use `git fetch`

* [Getting changes from a remote repository](https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository)
