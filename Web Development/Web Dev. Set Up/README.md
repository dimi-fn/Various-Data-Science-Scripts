# Web Dev. Set Up

Contents
=======================

* [node.js](#node.js)
* [Chocolatey](#chocolatey)


-----

# node.js

* `node.js` runtime is what your JavaScript code will understand in order to execute it and produce a result.

* `npm` package manager is a tool which allows you to install third party libraries, e.g. via `npm install <package-library>`

**Installation**:

When you [install node.js](https://nodejs.org/en/download/), this will give you both node.js (node.js command prompt) and npm, and if you click on "automatic installation of additional tools" this will also install chocolatey. Confirm your node installation by running on Git Bash:
* `node -v`, `npm -v`, `npx -v`

------

# Chocolatey

* [Chocolatey](https://chocolatey.org/) is a popular open source package manager for Windows applications. It simplifies Windows software lifecycle management, ie.,from installation of a software to its upgrade and uninstallation.
    * before installing it:
        * open powershell in admin and run: `Get-ExecutionPolicy`. If it returns Restricted or Undefined run: `Set-ExecutionPolicy Unrestricted`
    * install Chocolatey
    * to ensure that installation was successful
        * on PowerShell run `choco`
        * on Git Bash run `choco --help`, `choco --version`
    * upgrade Chocolatey before installing anything else via `choco upgrade chocolatey` on PowerShell on admin mode.
