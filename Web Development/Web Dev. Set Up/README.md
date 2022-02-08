# Web Dev. Set Up

Contents
=======================

* [Sync your VS Code Settings Between Multiple Devices](#sync-your-vs-code-settings-between-multiple-devices)
* [The .bashrc file](#the-bashrc-file)
* [Windows](#windows)
    * [Node.js](#nodejs)
    * [Chocolatey](#chocolatey)
    * [pyenv](#pyenv)
    * [Docker](#docker-windows)
        * [Installation](#installation-docker-windows) | [Windows Subsystem Linux (WSL)](#windows-subsystem-linux-wsl) | [Tutorials](#tutorials)
* [Linux](#linux)
    * [Docker](#docker-linux)
        * [Installation](#installation-docker-linux)


-----

# Sync your VS Code Settings Between Multiple Devices

* https://www.freecodecamp.org/news/how-to-sync-vs-code-settings-between-multiple-devices-and-environments/

-----

# The .bashrc file

The .bashrc file is a bash shell script file in which you can put customized commands like aliases, 
* [What is the .bashrc file](https://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work)

To set up your .bashrc file and create your aliases:
* navigate to home directory: `cd ~`, i.e. navigate at C:\Users\"yourUser"
* search if the .bashrc file exists, otherwise create with: `touch .bashrc` and open it
* create aliases in the form: `alias <my-customized-command>='<the-actual-command>` (n.b. in bash scripts there are no spaces between words), save the file and reload Git Bash so that the customized commands are activated

-----

# Windows

## Node.js

* `node.js` runtime is what your JavaScript code will understand in order to execute it and produce a result.

* `npm` package manager is a tool which allows you to install third party libraries, e.g. via `npm install <package-library>`

<h3 id="installation-docker-windows">Installation</h2>

When you [install node.js](https://nodejs.org/en/download/), this will give you both node.js (node.js command prompt) and npm, and if you click on "automatic installation of additional tools" this will also install chocolatey. Confirm your node installation by running on Git Bash:
* `node -v`, `npm -v`, `npx -v`

**Upgrade**:

For Windows, run PowerShell as Administrator and run:

    Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
    npm install -g npm-windows-upgrade
    npm-windows-upgrade

, or download the latest installer package file by re-downloading node.js again.

------

## Chocolatey

* [Chocolatey](https://chocolatey.org/) is a popular open source package manager for Windows applications. It simplifies Windows software lifecycle management, ie.,from installation of a software to its upgrade and uninstallation.
    * before installing it:
        * open powershell in admin and run: `Get-ExecutionPolicy`. If it returns Restricted or Undefined run: `Set-ExecutionPolicy Unrestricted`
    * [install Chocolatey](https://chocolatey.org/install)
    * to ensure that installation was successful
        * on PowerShell run `choco`
        * on Git Bash run `choco --help`, `choco --version`
    * upgrade Chocolatey before installing anything else via `choco upgrade chocolatey` on PowerShell on admin mode.

------

### pyenv

Pyenv is a tool so that you can have control of your Python versions by easily switch between different Python version (it can be helpful when collaborating across projects with other developers)

**Download**:

* Open Git bash on admin: `$ choco install pyenv-win`
* confirm successful installation: on git bash run: `$ pyenv --version`
* `$ pyenv update` so that pyenv can update the list of the latest Python versions
* `$ pyenv install <latest stable Python version or any other desired version>`
* `$ pyenv global <the version you used above>` - [doc](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global)
* `$ pyenv rehash` - [doc](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-rehash)
* confirm python version `$ python --version` and version number for `$ python -m pip --version`

--------

<h2 id="docker-windows">Docker</h2>

## Installation

* [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
    * test installation via command line: `$ docker run hello-world`

## Windows Subsystem Linux (WSL)   

While downloading docker, you will be asked to [download the Linux kernel update package](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package). You can also [install on Windows a Linux distribution](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-6---install-your-linux-distribution-of-choice) of your choice and use a Linux terminal to run commands.
* [Best practices for setting up a WSL development environment](https://docs.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)

Access you file storage for Linux while being on WSL via Windows:
* open your Linux terminal on Windows and run: `explorer.exe .` | [info](https://superuser.com/questions/1185033/what-is-the-home-directory-on-windows-subsystem-for-linux), [info](https://docs.microsoft.com/en-us/windows/wsl/setup/environment#file-storage)

## Tutorials

* https://docs.docker.com/get-started/
* [The Docker Handbook – 2021 Edition - by freecodecamp](https://www.freecodecamp.org/news/the-docker-handbook/)
* [DevOps Engineering Course for Beginners - by freecodecamp](https://www.youtube.com/watch?v=j5Zsa_eOXeY&ab_channel=freeCodeCamp.org)
* [From Docker Desktop to Deployment - by Travis Media](https://www.youtube.com/watch?v=i7ABlHngi1Q&ab_channel=TravisMedia)
* [Learn Docker - DevOps with Node.js & Express - by freecodecamp](https://www.youtube.com/watch?v=9zUHg7xjIqQ&ab_channel=freeCodeCamp.org)
* [Deploy 12 apps to AWS, Azure, & Google Cloud](https://www.youtube.com/watch?v=-ANCcFQBk6I&ab_channel=freeCodeCamp.org)

-------

# Linux

* [Basic set up for git](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Git%20%26%20GitHub#linux)
* [SSH key](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Git%20%26%20GitHub#ssh-key-linux--windows)
    * [more on SSH keys on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1604)

-------

<h2 id="docker-linux">Docker</h2>


<h3 id="installation-docker-linux">Installation</h2>
[Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
