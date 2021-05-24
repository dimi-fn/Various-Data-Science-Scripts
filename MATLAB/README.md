# MATLAB

Contents
=======================

* [Commands](#commands)
* [Desktop & Editor](#desktop--editor)
* [Vectors & Matrices](#vector--matrices)

-------

# Commands

* Use the Up arrow to see previous commands
    * `clear` to empty workspace / `clc` to empty the Command Window
    * `load <filename.mat>` to load again the variables of the file
        * load only one variable from a .mat file containing multiple variables: `load someFile x`

* MATLAB variables are case sensitive. They should start with a letter and contain only letters, numbers, and underscores

* Save files: `save filename.mat`
    * `.m` files are like .py files in Python, whereas .mlx files (live scripts that contain the code, the output, and the formatted text together in the Live Editor) are like .ipynb files

* If you add a semicolon `;` to the end of a command, the result will not be displayed, however, the result of that command will be displayed in the Workspace window as usual.

* MATLAB does not rerun previous commands in the Command Window (you need to repeat the command for any variable changes)

* Use `format long` to display all decimal places

**Built-in constants**:
* pi (for π)

* `i` is an imaginary number, a built-in constant in MATLAB

**Built-in functions**:
* `abs()`, `sqrt()` `eig()` (eigenvalues), `sin()` (sine)

* Use parentheses to pass inputs to functions, e.g.: y = sin(x)

-------

# Desktop & Editor

1) Current folder
2) Command Window 
3) Workspace

* To organize all commands and their output: "New live script" in the toolstrip
    * add "Code" or "Text" for description
    * saving the live script will save the code, output, and descriptions
    * you can click "workspace" to view variables in workspace gets minimized after commands execution

-------

# Vectors & Matrices




-------

## Sources

[1] https://matlabacademy.mathworks.com/