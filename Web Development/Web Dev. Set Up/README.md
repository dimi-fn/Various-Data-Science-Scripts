# Web Dev. Set Up

Contents
=======================

* [Windows](#windows)
    * [Node.js](#nodejs)
    * [Chocolatey](#chocolatey)
    * [pyenv](#pyenv)
    * [Docker](#docker)

-----

# Windows

## Node.js

* `node.js` runtime is what your JavaScript code will understand in order to execute it and produce a result.

* `npm` package manager is a tool which allows you to install third party libraries, e.g. via `npm install <package-library>`

**Installation**:

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

# Docker

## Installation

* [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
    * test installation via command line: `$ docker run hello-world`


## Tutorials

* [The Docker Handbook – 2021 Edition - by freecodecamp](https://www.freecodecamp.org/news/the-docker-handbook/)
* [DevOps Engineering Course for Beginners - by freecodecamp](https://www.youtube.com/watch?v=j5Zsa_eOXeY&ab_channel=freeCodeCamp.org)
* [From Docker Desktop to Deployment - by Travis Media](https://www.youtube.com/watch?v=i7ABlHngi1Q&ab_channel=TravisMedia)
* [Learn Docker - DevOps with Node.js & Express - by freecodecamp](https://www.youtube.com/watch?v=9zUHg7xjIqQ&ab_channel=freeCodeCamp.org)
* [Deploy 12 apps to AWS, Azure, & Google Cloud](https://www.youtube.com/watch?v=-ANCcFQBk6I&ab_channel=freeCodeCamp.org)
