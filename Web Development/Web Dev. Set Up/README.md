# Web Dev. Set Up

Contents
=======================

* [Sync your VS Code Settings Between Multiple Devices](#sync-your-vs-code-settings-between-multiple-devices)
* [The .bashrc file](#the-bashrc-file)
* [Windows](#windows)
    * [Node.js](#nodejs-windows)
    * [Chocolatey](#chocolatey)
    * [pyenv & pipenv](#pyenv--pipenv)
    * [Docker](#docker-windows)
        * [Install](#install-docker-windows) | [Windows Subsystem Linux (WSL)](#windows-subsystem-linux-wsl) | [Tutorials](#tutorials)
* [Linux](#linux)
    * [Basic Setup & Various](#basic-setup--various)
    * [Node.js](#nodejs-linux)
    * [pyenv](#pyenv-linux)
    * [Docker](#docker-linux)
        * [Install](#install-docker-linux)


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

<h2 id="nodejs-windows">Node.js</h2>

* `node.js` runtime is what your JavaScript code will understand in order to execute it and produce a result.

* `npm` package manager is a tool which allows you to install third party libraries, e.g. via `npm install <package-library>`

### Install & Upgrade

**Install**:

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

<!-- <h2 id="pyenv-windows">pyenv</h2> -->

## pyenv & pipenv

Pyenv is a tool so that you can easily install multiple versions and be able to switch between them (it can be quite helpful when collaborating across projects with other developers).

### Pyenv

* Open Git bash on admin: `$ choco install pyenv-win`
* confirm successful installation: on git bash run: `$ pyenv --version`
* `$ pyenv update` so that pyenv can update the list of the latest Python versions
* check installation by checking the list of all available python versions: `pyenv install --list`
* `$ pyenv install <latest stable Python version or any other desired version to install>`
* `$ pyenv global <the version you chose to install>` - [doc](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global)
* in home directory:`$ pyenv rehash` - [doc](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-rehash) to update pyenv with the new settings
* confirm python version `$ python --version` and version number for `$ python -m pip --version`
* update pyenv: `pip install --upgrade pyenv-win`
    * [How to update pyenv](https://github.com/pyenv-win/pyenv-win#how-to-update-pyenv)

<br>

* [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/)
* [Pyenv in Windows](https://dev.to/dendihandian/pyenv-in-windows-4lpe)

### Pipenv

* Install **pipenv**:
    * run cmd with admin rights
    * `pip install pipenv`
    * `pipenv --version`
* to upgrade pipenv: `pip install --upgrade pipenv` 
* Usage:
    * `pipenv install` to install packages
    * `pipenv install --dev` to install dev packages
    * `pipenv run dev` to run the dev commands from the Pipfile

<br>

* [Edit environment variables on Windows](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)

--------

<h2 id="docker-windows">Docker</h2>

Docker is an open platform for developing, shipping, and running applications. [Docker overview](https://docs.docker.com/get-started/overview/)

<h3 id="install-docker-windows">Install</h2>

* [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
    * test installation via command line: `$ docker run hello-world`
    * check version: `docker --version`

## Windows Subsystem Linux (WSL)   

While downloading docker, you will be asked to [download the Linux kernel update package](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package). You can also [install on Windows a Linux distribution](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-6---install-your-linux-distribution-of-choice) of your choice and use a Linux terminal to run commands. Follow the [WSL installation guide](https://docs.microsoft.com/en-us/windows/wsl/install)
* on PowerShell check the WSL version: `wsl -l -v`
* [Best practices for setting up a WSL development environment](https://docs.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)

Access you file storage for Linux while being on WSL via Windows:
* open your Linux terminal on Windows and run: `explorer.exe .` | [info](https://superuser.com/questions/1185033/what-is-the-home-directory-on-windows-subsystem-for-linux), [info](https://docs.microsoft.com/en-us/windows/wsl/setup/environment#file-storage)

**VS Code**:

 Download the extention "Remote - Containers" which lets you use a Docker container as a full-featured development environment.
 * [Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)


## Tutorials

* https://docs.docker.com/get-started/
* [The Docker Handbook – 2021 Edition - by freecodecamp](https://www.freecodecamp.org/news/the-docker-handbook/)
* [DevOps Engineering Course for Beginners - by freecodecamp](https://www.youtube.com/watch?v=j5Zsa_eOXeY&ab_channel=freeCodeCamp.org)
* [From Docker Desktop to Deployment - by Travis Media](https://www.youtube.com/watch?v=i7ABlHngi1Q&ab_channel=TravisMedia)
* [Learn Docker - DevOps with Node.js & Express - by freecodecamp](https://www.youtube.com/watch?v=9zUHg7xjIqQ&ab_channel=freeCodeCamp.org)
* [Deploy 12 apps to AWS, Azure, & Google Cloud](https://www.youtube.com/watch?v=-ANCcFQBk6I&ab_channel=freeCodeCamp.org)

-------

# Linux

## Basic Setup & Various

* [Basic set up for git](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Git%20%26%20GitHub#linux)
* [SSH key](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Git%20%26%20GitHub#ssh-key-linux--windows)
    * [more on SSH keys on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1604)
* [Install HomeBrew](https://brew.sh/), [How to Install Brew on Ubuntu](https://www.how2shout.com/linux/how-to-install-brew-ubuntu-20-04-lts-linux/)
    * [Homebrew installs the stuff you need that Linux or Apple didn't](https://formulae.brew.sh/formula/)    

-------

<h2 id="nodejs-linux">Node.js</h2>

* [How To Install Node.js on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04)
* Install the Node Version Manager [nvm](https://github.com/nvm-sh/nvm/blob/master/README.md) 
    * [install](https://github.com/nvm-sh/nvm/blob/master/README.md#installing-and-updating)
    * [Verify Installation](https://github.com/nvm-sh/nvm/blob/master/README.md#verify-installation)
* [Upgrade Node.js](https://phoenixnap.com/kb/update-node-js-version)
* [Upgrade npm](https://stackoverflow.com/questions/23393707/how-to-update-npm)
    
-------

<h2 id="pyenv-linux">pyenv</h2>

* having installed brew from [basic setup & various](#basic-setup--various), run: `brew install pyenv` | [How to install Pyenv on Ubuntu](https://medium.com/@marine.ss/installing-pyenv-on-ubuntu-20-04-c3a609a20aa2)
    * additional: `brew install openssl readline sqlite3 xz zlib`

* add pyenv init to your shell 
    * find your config file; navigate home directory `cd ~`, `ls -lah`. Your shell config file should be one of: .zshrc, .bash_profile, .bashrc
        * `echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.<put here your config file>`

* [How to update pyenv](https://github.com/pyenv-win/pyenv-win#how-to-update-pyenv)

* [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/)

--------

<h2 id="docker-linux">Docker</h2>

<h3 id="install-docker-linux">Install</h2>

* [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

* [Upgrade Docker Engine](https://docs.docker.com/engine/install/ubuntu/#upgrade-docker-engine)

* check version: `docker --version`

* **VS Code**: Download the extention "Remote - Containers" which lets you use a Docker container as a full-featured development environment.
    * [Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)
