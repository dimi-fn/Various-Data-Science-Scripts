Contents
=======================

* [Reasons to Use Virtual Environment (venv)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#reasons-to-use-virtual-environment-venv)
* [Requirements](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#requirements)
* [Set up (on Windows)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#set-up-on-windows)
* [requirements.txt](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#requirementstxt)
* [General Notes](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#general-notes)
* [Sources](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#sources)


### Reasons to Use Virtual Environment (venv)

Different projects require different packages and sometimes different versions of packages, therefore it is highly recommended to set up your projects in a virtual environment where the above can be achieved, maintained, and scaled for other developers.

### Requirements

Have python installed on your system.

### Set up (on Windows)

- Create a folder somewhere in your system where your virtual env project will take place. Let's suppose the creation 
of a folder called: "Virtual_project" (i.e., via cmd C:\Users\the path you choose\ --> mkdir Virtual_project)

- Being in the above path, type in the cmd: python -m venv "your_project_name". Let's suppose you want the name of your venv project to be "my_venv_project", then: via cmd C:\Users\the path you chose\Virtual_project --> python -m venv my_venv_project
    * You will now see that 3 folders were created ("Include", "Lib", "Scripts") and one file ("pyenv.cfg").

- To activate your virtual environment: 
    * navigate inside the project path (C:\Users\the path you chose\Virtual_project\my_venv_project).
    * Navigate inside "Scripts" (cd Scripts).
    * Type: activate.bat
    * Now you will notice the change in the start of your path in the cmd (it starts with "(my_venv_project) C:\Users\..\"), and the venv environment is now activated.
        
        * If you type "where python", the 1st will be the venv path.
        * If you type "*pip list*", you will only see pips of the venv (**venv pips**), which would probably be "pip" and "setuptools". Notice that if you "pip list" outside your venv, then you will understand the difference by viewing the list of packages installed on your system installation of Python (**global pips**).
        * If you type "*pip freeze*", you will only see the pips of the venv that you will be installing from now on. In this case, you will see nothing, since you haven't installed any packages on this new venv.

- Now you can install pip packages, which will only be installed here, with pip install "new package"

* Look at the very left part of the path, to make sure you are navigating in the venv environment

* Suppose you type "pip install pandas", installing the pandas packages by being in your venv project (C:\Users\the path you chose\Virtual_project\my_venv_project  --> pip install pandas). This will install pandas only in this virtual environment.
    * Now, if you "pip list" you will also see pandas installed (along with the default 2 pips).
    * If you "pip freeze", you will only see the pandas package, as this was the only pip executed in this very virtual environment. Another difference is that the output of pip freeze generates the versions of the packages in the right format, which is useful later on for the *requirements.txt*.
    * The above explains the *difference between pip list and pip freeze*.

- To deactivate your venv:
* deactivate.bat

- To delete your venv:
* delete the directory with rmdir "directoy_name" /s, or just delete the virtual environment folder manually.

### requirements.txt

In order to create requirements.txt: 

* Go to your venv project path.
* Check your installed-only for this project packages via: "pip freeze"
* Save those with the command **"pip freeze > requirements.txt"** (this grabs the packages created in this venv project
with the right format of "package"=="version_number", and it creates a txt file with those requirements).

* In order to "paste" those into another project:
	* copy that txt called "requirements.txt" into the folder of the new project (e.g. a new venv-environment project), in the "Scripts" subfolder.
	* cmd: *pip install -r requirements.txt*
		* This will install the particular packages along with their specific versions of the previous developer.

### General Notes:

- You should not commit the venv on Github.

- You should not put project files, i.e. python scripts in the venv folders.

- You should commit the "requirements.txt".

- To create a venv workspace with already installed the global-system packages:
after having created an empty folder at which the virtual env project will take place, type: "python - venv 'my_venv_name --system-site-packages'".

* After this, whatever package you install will not affect (neither add nor remove your global-system packages), you just began your project with installed your already installed packages from your system.

### Sources

[1] https://www.youtube.com/watch?v=APOPm01BVrk&ab_channel=CoreySchafer

[2] https://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list

[3] https://note.nkmk.me/en/python-pip-install-requirements/