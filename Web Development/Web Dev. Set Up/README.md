# Web Dev. Set Up

* [Chocolatey](https://chocolatey.org/): popular open source package manager for Windows applications. It simplifies Windows software lifecycle management, ie.,from installation of a software to its upgrade and uninstallation.
    * before installing it:
        * open powershell in admin and run: `Get-ExecutionPolicy`. If it returns Restricted or Undefined run: `Set-ExecutionPolicy Unrestricted`
    * install Chocolatey
    * to ensure that installation was successful
        * on PowerShell run `choco`
        * on Git Bash run `choco --help` 
    * upgrade Chocolatey before installing anything else via `choco upgrade chocolatey` on PowerShell on admin mode.
