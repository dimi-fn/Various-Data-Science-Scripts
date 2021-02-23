Contents
=======================

* [Reasons to Use Virtual Environment (venv)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#reasons-to-use-virtual-environment-venv)
* [Requirements](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#requirements)
* [Set up on Windows](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#set-up-on-windows)
* [Set up on Linux](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#set-up-on-linux)
* [requirements.txt](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#requirementstxt)
* [General Notes](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#general-notes)
* [Sources](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#sources)

### Reasons to Use Virtual Environment (venv)

Different projects require different packages and sometimes different versions of packages, therefore it is highly recommended to set up your projects in a virtual environment where the above can be achieved, maintained, and scaled for other developers.

### Requirements

Have python installed on your system. On linux you will firstly need to install via terminal: "sudo apt-get install python3-venv".

### Set up on Windows

1. Create your **project environment**: create a folder somewhere in your system where your project will take place. Let's suppose the creation 
of a folder called: "venv_project", then cmd C:\Users\the path you choose\ --> mkdir venv_project).

2. Create your **virtual environment**: being in the above path, i.e. C:\Users\the path you have chosen\venv_project -->type-->

    `python -m venv` "**your_venv_name**"

    Let's suppose you want the name of your virtual environment to be called "venv1", then via cmd being at C:\Users\the path you have chosen\Virtual_project -->type--> 
    
    `python -m venv venv1`

3. You will have successfully created your virtual environment if you are seeing three folders named "**Include**", "**Lib**", "**Scripts**", and one "**pyenv.cfg**" file created inside the venv directory.

- To **activate** your virtual environment: 
    * navigate inside the project path (C:\Users\the path you have chosen\project\venv1)
    * Navigate inside "Scripts", via cd Scripts (C:\Users\the path you have chosen\project\venv1\Scripts)
    * Type: `activate.bat`
    * You will now notice the change in the start of your path in the cmd (it starts with "(venv1) C:\Users\..\"), and the virtual environment is now activated.
        
        * If you type "*where python*", the 1st will be the venv path.
        * If you type "`pip list`", you will only see pips of the venv (**venv pips**), which would probably be "pip" and "setuptools". Notice that if you "pip list" outside your venv, then you will understand the difference by viewing the list of packages installed on your system installation of Python (**global pips**).
        * If you type "`pip freeze`", you will only see the pips of the venv that you will be installing from now on. In this case, you would now be seeing nothing since you haven't installed any packages on this venv yet.

- Now you can install pip packages, which will only be installed here, with pip install "package".

* You can always make sure you are navigating in the venv environment by looking at the very left part of the path

* Suppose you type "pip install pandas", installing the pandas packages by being in your venv project (C:\Users\the path you have chosen\project\venv --> pip install pandas). This will install pandas only in this virtual environment.
    * Now, if you "*pip list*" you will also see pandas installed (along with the two default pips).
    * If you "*pip freeze*", you will only see the pandas package, as this was the only pip executed in this virtual environment. Another difference is that the output of pip freeze generates the versions of the packages in the right format, which is useful later on for the *requirements.txt* file creation and extraction.
    * The above explains the main *difference between pip list and pip freeze*.

- To **deactivate** your venv:
    * deactivate.bat (C:\Users\the path you have chosen\project\venv1\Scripts\deactivate.bat)

- To **delete** your venv:
    * delete the directory with rmdir "project" /s, or just delete the virtual environment folder manually.

### Set up on Linux

Same rationale exists with that of the set up on windows. Check the [requirements](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Virtual_Env#requirements).

Main differences here are:
- Instead of the directory "Scripts", activate the venv through the "bin" folder via the command: "source 'path to project'/'name of venv'/bin/activate, i.e. for the example on windows do: $ source 'the path you have chosen'/project/venv1/bin/activate

- To deactivate: $ deactivate

### requirements.txt

In order to create requirements.txt: 

* Go to your venv project path.
* Check your installed-only for this project packages via: "`pip freeze`".
* Save those with the command "`pip freeze > requirements.txt`" (this grabs the packages created in this venv project
with the right format of "package"=="version_number", and it creates a requirements.txt text file with those requirements).

* In order to "paste" those into another project:

    * You might want to transfer all packages and dependencies from one project to another project or machine automatically and not just manually. After creating a new venv to the new project/machine, if you do "pip freeze" you won't see any pip installed as expected.
	* paste that txt file called "requirements.txt" into the folder of the new project, in its "Scripts" subfolder.
	* cmd: `pip install -r requirements.txt` to **install the packages**.
		* This will install the particular packages along with their specific versions of the previous developer.
        * If you now type "pip freeze", you will notice that all packages with their respective versions of the previous project/developer have successfully been transferred and installed.

### General Notes:

- You may want to put your venv inside your project folder, but you don't want to put any of your project files into the venv.
    * You should not put project files, e.g. python scripts, in the venv folders.

- You should not commit the venv on Github.
    * you can use .gitignore 

- You should commit the "requirements.txt", which would help other developers create the necessary environment to run your project (there is no need to commit the entire env, as written above).

- To create a venv workspace with your existing installed global-system packages:
After having created your project directory at which the venv will take place, type:
"**python -m venv 'my_venv_name' --system-site-packages**"
    * After that, whichever packages you install will not affect (neither add nor remove your global-system packages). In other words, you will begin your project by "borrowing" the packages that are already installed at your system, without altering them globally if you do changes locally at a later stage.
    * Use "**pip list --local**" for the same use as "pip list" previously.
    * Use "**pip freeze --local**" for the same use as "pip freeze" previously.

### Sources

[1] https://www.youtube.com/watch?v=APOPm01BVrk&ab_channel=CoreySchafer

[2] https://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list

[3] https://note.nkmk.me/en/python-pip-install-requirements

[4] https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/

[5] https://docs.microsoft.com/en-us/visualstudio/python/selecting-a-python-environment-for-a-project?view=vs-2019#use-virtual-environments