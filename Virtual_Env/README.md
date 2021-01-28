Contents
=======================

* [Reasons to Use venv](#reason)
* [Requirements](#requirements)
* [Set Up](#set-up)
* [Requirements.txt](#requirements.txt)
* [General Notes](#general-notes)
* [Sources](#sources)

---

### Reason

Different projects require different packages and sometimes different versions of packages, therefore it is highly recommended to set up your projects in virtual environment where the above can be achieved, maintained and scaled for other developers.

### Requirements

Have python installed at your system.

### Set up (on Windows)

- create a folder somewhere at your system where your virtual env project will take place. Let's suppose the creation 
of a folder called: "Virtual_project" (i.e., via cmd C:\Users\the path you choose\ --> mkdir Virtual_project)

- create venv: go to the directory of your "Virtual_project" folder, and create a subfolder where your virtual environment project will take place. Suppose subfolder "my_venv_project" (i.e., via cmd C:\Users\the path you chose\Virtual_project --> mkdir my_venv_project)

- being in the above path, type: python -m venv "your_project_name", hence in this case let's suppose --> python -m venv my_first_venv_project
* You will now see the 3 folders created ("Include", "Lib", "Scripts") and one file ("pyenv.cfg").

- to activate your virtual environment: 
* navigate inside the project path (C:\Users\the path you chose\Virtual_project\my_venv_project).
* navigate inside "Scripts" (cd Scripts).
* type: activate.bat
* Now you will notice the change in the start of your path in the cmd (it starts with "(my_venv_project) C:\Users\..\").
**if you type "where python", the 1st will be the venv path.
** if you do pip list, you will only see pips of the venv.
** if you do pip freeze, you will only see the pips of the venv that you will be installing from now on.

- now you can install pip packages, which will only be installed here, with pip instal "new package"
* look at the very left part of the path, to make sure you are navigating in the venv environment
* suppose you type "pip install pandas", installing the pandas packages being in your venv project (C:\Users\the path you chose\Virtual_project\my_venv_project  --> pip install pandas). This will install pandas only in this virtual environment.

- to deactive your venv:
* deactivate.bat

- to delete your venv:
* delete the directory with rmdir "directoy_name" /s, or just delete the virtual environment folder manually.

### requirements.txt

* in order to create requirements.txt: be in the path inside the venv
* check your installed-only for this project packages with "pip freeze"
* save those with "pip freeze > requirements.txt" (this grabs the packages created in this venv project
with the right format of "package"=="version_number")

* in order to "paste" those into another project:
	* copy that txt called "requirements.txt" into the folder of the new project (e.g. a new venv-environment project), in the "Scripts" subfolder
	* pip install -r requirements.txt
		* this will install the particular packages and their specific versions of the previous developer

### General Notes:

- You should not commit the venv in github
- You should not put project files, i.e. python scripts in the venv folders
- You should commit the requirements.txt
- To create a venv workspace with already installed the global-system packages:
after having created an empty folder at which the virtual env project will take place, type: "python - venv 'my_venv_name --system-site-packages'"
* After this, whatever package you install will not affect (neither add nor remove your global-system packages), you just began your project with installed your already installed packages from your system.

### Sources

[1] https://www.youtube.com/watch?v=APOPm01BVrk&ab_channel=CoreySchafer

[2] https://stackoverflow.com/questions/18966564/pip-freeze-vs-pip-list

[3] https://note.nkmk.me/en/python-pip-install-requirements/