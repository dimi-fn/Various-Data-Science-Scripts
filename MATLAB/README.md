# MATLAB

Contents
=======================

* [Commands](#commands)
* [Desktop & Editor](#desktop--editor)
* [Vectors & Matrices](#vectors--matrices)
    * [Evenly-Spaced Vectors](#)

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

All MATLAB variables are arrays. 
* scalars (i.e., single number containing 1 row and 1 column)
* matrices
    * row vectors and column vectors

* Arrays can be used to store related data in one variable.

* Examples
    * scalar: `x = 4` --> `arr = np.array(4)` in Python
    * row vector 1x2: `x = [5 , 9]` or `x = [5 9]` --> `arr = np.array([5, 9])` in Python
    * column vector 2x1 `x = [5;9]` --> `arr = np.array([[5], [9]])` in Python 


    * matrix of 2x3: `x= [1,3,5;2,4,6]` --> 1st row==[1,3,5], 2nd row==[2,4,6]

## Evenly-Spaced Vectors
    * evenly-row spaced vector: `x = [1:4]` or `x= 1:4` or `x=[1,2,3,4]` | `:` is **inclusive** [inclusive, inclusive]




-------

## Sources

[1] https://matlabacademy.mathworks.com/