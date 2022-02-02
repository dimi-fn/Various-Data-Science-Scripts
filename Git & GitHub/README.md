# Git & GitHub

Git is a free and open-source version control system. 
* Git is the tool that tracks the changes in your code, whereas GitHub is a website where you host all of your Git repositories online (remotely on the website's cloud)

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
* [Check Git Status](#check-git-status)
* [Git Commands](#git-commands)
* [Git Workflow](#git-workflow)
* [Fork & Pull Request](#fork--pull-request)
* [Branching](#branching)
* [Miscellaneous](#miscellaneous)
* [Useful Sources](#useful-sources)

------

# Documentation

* [Git doc](https://git-scm.com/)
* [Hello Git - Github](https://docs.github.com/en/get-started/quickstart/hello-world)
* [Introduction to GitHub in Visual Studio Code](https://docs.microsoft.com/en-us/learn/modules/introduction-to-github-visual-studio-code/)
* [SSH protocol](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)

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

The are four ways to do that:

* 1st way: 
    * Github: Create your repo on github and copy the repo HTTPS URL 
    * VS Code: source control > open folder (to create a workspace directory) > (git bash, by being under your project directory:) git clone 'the_HTTPS_URL'
        * if you didn't create your README.md file from the 1st step:
            * 'git add' or 'git add .' > 'git commit -m "your commit message"' > git push

* 2nd way (similar to the 1st way but without the terminal):
    * Github: Create your repo on github and copy the repo HTTPS URL 
    * source control: clone repository > paste the HTTPS repo URL > choose workspace directory > commit any potential changes through the CLI of VS Code > push via the publish button in the bottom

* 3rd way (integrate all steps above into one via VS Code - it prerequires that you have already linked your GitHub on VS Code): 
    * VS Code: source control > open folder (to create a workspace directory) > 'new file' to add e.g. your README.md file > (source control:) publish to Github (there's no need to initialize the repo on GitHub since this will automatically be created there) > choose public/private repo and choose the files to be uploaded on GitHub

* 4th way
    * Github: Create an empty repo on github and copy the repo HTTPS URL 
    *  VS Code: open folder (to create a workspace directory) or you can do that via your terminal > add any initial files, e.g. README.md > (git bash, navigate under current working directory:) 'git init' (this will create the .git hidden file) > 'git add' or 'git add .' if more than one file > git commit -m "your message" > git remote add origin "here paste the repo HTTPS URL" (via 'git remote -v' you can check you did that right) > git push --set-upstream origin master

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

# Check Git Status
* `git log`: git history of current branch (type "q" to exit)
* `git log --oneline --graph`
* `git status`: displays staged changes, unstaged changes and untracked files on working tree

------

# Git Commands

* `clone`: bring a repo that is hosted somewhere like github into a folder (directory) on your local machine
* `add`: track your files and changes in Git
* `commit`: save your files in Git
* `push`: upload Git commits remotely, e.g. on Github
* `pull`: download changes from a remote repo to your local machine, i.e. the opposite of "push"

------

# Git Workflow

Firstly, you have to synchronize your local repo with the remote repo hosted e.g. on GitHub.

* write code
* `git add` or `git add file1 file2` or `git add .` to add all files (stage changes)
    * when you do 'git add', you copy a file from the working directory into the staging area. An *index* file is created under the *hooks* folder of the .git hidden file
* `git commit`: commit changes
    * when you 'git commit' then a new folder is created under the *objects* folder of the .git folder encompassing the git log hash. You can view the 7 out of the 40 letters and numbers of the hash in the commit terminal message
    * To undo a commit:
        * `git checkout here-type-the-commit-hash`
* `git push`: push changes remotely

------

# Fork & Pull Request
* `Fork the repo`
    * fork the repo from the owner's github repo page. This will automatically create a forked repo on your personal github
* `Clone the forked repo` (i.e. the remote repo now hosted on your personal github) so that you can apply the desired changes. One way you can do that is:
    * grab the clone url: forked repo page > "Code" > "HTTPS" > copy the URL which ends with '.git'
    * in VS code: source control > clone > enter the URL > create workspace folder. Now you have a forked repo at your system
        * now you can apply the changes in the code. Commit the changes and push (these, as expected, will be applied only on your forked repo)
* `Submit pull request to the project owner`      
    * navigate to the forked repo hosted on your personal github account > new pull request > create a new pull request
        * you can verify that by visiting the pull requests section of the original associated project

**Refresh changes from the remote (original) repository**

Let's suppose you have already forked a repo, and then submitted a pull request. What if you want to submit another pull request at a later time point? By that time, the remote repo might have changed, and those changes would not have been applied to your forked repo which would remain outdated. Hence, in order to refresh those changes before you submit a new pull request

1) use `git fetch` to refresh the changes 

* [Getting changes from a remote repository](https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository)

-------

# Branching

* `git branch`
    * view all branches

* `git checkout`
    * switch between branches
        * if you do that via git bash (and not e.g. via the command palette of VS Code) then VS Code will get automatically updated (see at the bottom left for the current branch)

* `git checkout -b <name-of-new-branch>`
    * create a new branch

* `git push --set-upstream origin <name-of-the-branch-you-created-just-earlier>`
    * publish the new branch. This needs to done once per new branch. After this step, you can commit changes of this branch with only 'git push' until its merge with the master branch

* `git branch -d <branch-name>`
    * delete a branch locally

* `git push -d origin <branch-name>`
    * delete a branch remotely (on Github)
        * when you `git branch -d <branch-name>` the branch will be deleted locally but it will still remain on Github, therefore via `git push -d origin <branch-name>` you can delete the branch remotely as well

<br>

    git branch -d <branch-name> # delete branch locally
    git push -d origin <branch-name> # delete branch remotely    

* `git diff <branch-name>`
    * display the difference between current branch and 'branch-name'

* `git merge <branch-name>`
    * under the master branch, merge the master branch with the branch 'branch-name'
    * you then need to `git push` in order to successfully apply the merge

-------

# Miscellaneous

* Git bash:
    * copy with: Control + Insert
    * paste with: Shift + Insert

* [various terminal commands](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Shell%20Scripting)    
    * `ls -a` to also display hidden files, e.g. the .git file
    * `.` means the current directory
    * `..` means the parent dir of `.`, i.e. the directory that contains it

------

# Useful Sources

* [Documentation](#documentation)
* [Cheatsheets](#cheatsheets)
* https://www.youtube.com/watch?v=RGOj5yH7evk&ab_channel=freeCodeCamp.org
