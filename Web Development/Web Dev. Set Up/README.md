# Web Dev. Set Up

Contents
=======================

* Windows
    * [Node.js](#nodejs)
    * [Chocolatey](#chocolatey)
    * [pyenv](#pyenv)


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

* Open Git bash on admin: `choco install pyenv-win`
* confirm successful installation: on git bash run: `pyen --version`
* `$ pyenv update` so that pyenv can update the list of the latest Python versions
* `$ pyenv install <latest stable Python version or any other desired version>`
* `$ pyenv global <the version you used above>` - [doc](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global)
* `$ pyenv rehash` - [doc](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-rehash)
* confirm python version `$ python --version` and version number for `$ python -m pip --version`


* [$ pyenv rehash](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-rehash)
