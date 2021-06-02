# MATLAB

Contents
=======================

* [MATLAB Documentation](#matlab-documentation)
* [Commands](#commands)
    * [Importing Data](#importing-data)
* [Desktop & Editor](#desktop--editor)
* [Vectors & Matrices](#vectors--matrices)
    * [Evenly-Spaced Vectors](#evenly-spaced-vectors)
    * [Array Creation Functions](#array-creation-functions)
* [Indexing into and Modifying Arrays](#indexing-into-and-modifying-arrays)
    * [Extracting Multiple Elements](#extracting-multiple-elements)
    * [Changing Values in Arrays](#changing-values-in-arrays)
    * [Logical Indexing](#logical-indexing)
* [Function Calls](#function-calls)
* [Visualization - Plotting](#visualization---plotting)
* [Programming Constructs](#programming-constructs)

-------

# MATLAB Documentation

Either by the "?" button or in the command line type `doc <something to search>`, e.g. [doc](https://www.mathworks.com/help/matlab/ref/doc.html) randi

------

# Commands

* Use the Up arrow to see previous commands
    * `clear` to empty workspace / `clc` to empty the Command Window

* % This is a comment on Matlab code cell    
    * Matlab **markdown** https://www.mathworks.com/help/matlab/matlab_prog/marking-up-matlab-comments-for-publishing.html
    
* `load <filename.mat>` to load again the variables of the file, then type <filename> to print the matrix
    * load only one variable from a .mat file containing multiple variables: `load filename x`
    * use command `usage` under `load <filename.mat>` to see the matrix after loading the file
    * use `data.VariableName` to extract a specific variable (feature / table value / column value) from the table

* **saving**: 
    * `save filename.mat`
    * `.m` files are like .py files in Python, whereas .mlx files (live scripts that contain the code, the output, and the formatted text together in the Live Editor) are like .ipynb files

* `which pathdef`: search path

* MATLAB variables are case sensitive. They should start with a letter and contain only letters, numbers, and underscores

* If you add a semicolon `;` to the end of a command, the result will not be displayed, however, the result of that command will be displayed in the Workspace window as usual.

* MATLAB does not rerun previous commands in the Command Window (you need to repeat the command for any variable changes)

* Use `format long` to display all decimal places

**Built-in constants**:
* pi (for π)

* `i` is an imaginary number, a built-in constant in MATLAB

**Built-in functions**:
* `abs()`, `sqrt()` `eig()` (eigenvalues), `sin()` (sine)

* Use parentheses to pass inputs to functions, e.g.: y = sin(x)

## Importing Data

* You can import .mat, .jpg, .txt, and .csv files by the "import data" tool
    * csv files can be stored in various ways. Missing data will be displayed with orange colour

* you can select column tables (**features**) via `tableName.columnName`

* you can interact with the table via the output table pane on the right
    * e.g. you can sort values, and then use the "update code" functionality

* you can **extract rows** by array indexing
    * e.g. to extract the first 4 rows and assign that to a variable: `x= tableName(1:4, :)` -->x will also be a table

**Note: *Single quotes create a character vector and double quotes create a string. In most cases, strings are preferable.*
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

**All MATLAB variables are arrays**. 
* scalars (i.e., single number containing 1 row and 1 column)
* vectors (1D)
* matrices (2D)
    * row vectors and column vectors

* Arrays can be used to store related data in one variable.

* Examples
    * scalar: `x = 4` --> `arr = np.array(4)` in Python
    * row vector 1x2: `x = [5 , 9]` or `x = [5 9]` --> `arr = np.array([5, 9])` in Python
    * column vector 2x1 `x = [5;9]` --> `arr = np.array([[5], [9]])` in Python 


    * matrix of 2x3: `x= [1,3,5;2,4,6]` --> 1st row==[1,3,5], 2nd row==[2,4,6]

| Example          | Description    | 
| ------------- |:-------------:| 
| 3      | scalar |     
| [3  5]  or [3,5]  | row vector |     
| [3;5]      | column vector |     
| [3 5 9 ; 0 2 4 ]     | matrix |     



## Evenly-Spaced Vectors

* **evenly-row spaced vector**: `x = [1:4]` or `x= 1:4` or `x=[1,2,3,4]` | `:` is **inclusive** [inclusive, inclusive]

* [**start** : `step` : **end**]: e.g. 1 to 10 with step 2 would be: `x =[1 : 2 : 10]` 
    * *whereas in Python step would be at the end*

* if you know the number of elements you want in a vector beforehand -> use `linspace(first,la1,1st,number_of_elements).`
    * `x = linspace(0,10,5)` will give 0, 2.5, 5, 7.5, and 10 which gives a row vector 1x5
    * use `transpose` to turn it into a column vector of 5x1: `x = x'` 

* create a column vector using a single command by creating a row vector and then transposing it all on one line.
    * `x = (4:2:10)'` will give a column vector 4x1, with the elements: 4,6,8,10

| Example          | Description    | 
| ------------- |:-------------:| 
| 2:5      | Create a vector from 2 to 5, spaced by 1, using the [colon (:)](https://www.mathworks.com/help/matlab/ref/colon.html) operator |     
| 4:2:10      | Create a vector from 4 to 10, with a step of 2 | 
| [linspace](https://www.mathworks.com/help/matlab/ref/linspace.html)1,20,5      | Create a vector with 5 elements, the values of which are evenly spaced from 1 to 20 | 

<br>

**Create Matrices**
| Example          | Description    | 
| ------------- |:-------------:| 
| [rand](https://www.mathworks.com/help/matlab/ref/rand.html)(2)    | Create a square matrix with 3 rows and 3 columns |     
| [zeros](https://www.mathworks.com/help/matlab/ref/zeros.html)(2,3)    | Create a rectangular matrix with 2 rows and 3 columns. |   

<br>

** Note: 
 If `linspace` or `:` is used to create a vector, then brackets ("[]") are not needed

## Array Creation Functions

* e.g., `x = rand(4)` will create a 4x4 matrix with random numbers
* Specify number of rows/columns, e.g., `x = rand(3,2)` will create a 3x2 matrix with random numbers
    * you can fill matrices containing only zeros or one using the `zeros()` and `ones()` functions respectively. E.g. `x = zeros(4,2)` will give a 4x2 matrix filled out with 0s


* Get the **size of an array**: `size(x)`
    * `[Xrow, Xcol] = size(X)` create two variables comprising the size of X

<br>

**Array Operations**
| Example          | Description    | 
| ------------- |:-------------:| 
|  [1 1 ; 1 1]*[2 2 ; 2 2] => will give 4, 4, 4, 4 | [Matrix Multiplication](https://www.mathworks.com/help/matlab/matlab_prog/array-vs-matrix-operations.html#btyv9yp-4)  |     
| [1 1 ; 1 1].*[2 2 ; 2 2] => will give 2, 2, 2, 2  | [Element-wise Multiplication](https://www.mathworks.com/help/matlab/matlab_prog/array-vs-matrix-operations.html#bu90xxy-1)   |

<br>

------

# Indexing into and Modifying Arrays

*Vectors: x(idx), Matrices: x(row, col)*

The **1st index position** starts at `1` (not 0 as in Python)

* e.g. `x(3) = 5`, will index the 3rd position element and change its value to 5

* extract a **range** of values, e.g. x=(2:4) (inclusive, inclusive)

* if you want to extract a **specifix element from a matrix**, e.g. the 3rd element in the first row, then: x=(1,3) (== 1st row, 3rd column)

* extract **all first row**: `x= (1:)`

* extract **all first column**: `x(:,1)`

* `end`: You can use the MATLAB keyword end as either a row or column index to reference the last element
    * e.g. if data the filename, then: `x = data(end, 2)` will return the the element which is located in the last row and in the 2nd column
    * `x = data(end-1, 3)` will give the scalar located in the second to last row in the 3rd column

| Example          | Description    | 
| ------------- |:-------------:| 
| M([end](https://www.mathworks.com/help/matlab/ref/end.html), 2)     | Access the element in the second column of the last row |     
| M(3,:)    | Access the entire 3rd row |     
| M(1:4,:) | Access all columns of the first four rows. |     
| A(2) = 10| Change the value of the second element of the array to 10 |     

<br>

## Extracting Multiple Elements

* grab all elements located in the 4th column: `x= data(:, 4)`

* grab all elements containing the last 3 columns: x = data(:, end-2:end)

## Changing Values in Arrays

* e.g. add a scalar value of 1 to all elements of an array (vector): `x2= x1 + 1;`

* add vectors of the same size, e.g. `v3 = v1+v2;`

* multiplication
    * `*` : matrix multiplication
    * `.*`: elementwise multiplication, e.g. x = [3,4] * [5,6] will give Error using  * Incorrect dimensions for matrix multiplication." ==> x = [3,4] .* [5,6]

## Logical Indexing

* True / False in MATLAB is expressed in 1 and 0 respectively
* and: `&`, or: `|`
    * e.g. x = v1(v1<8 & v1>4) will find values less than 8 and greater than 4

* you can compare a vector or matrix to a single scalar value using relational operators
    * e.g. [3 6 9] > 8 =>output=> 0 0 1

* choose a **subset** of array via a logical array
    e.g. : v2 = v1(v1>6) will assign to v2 all values for which v1>6 is true

* replace values: e.g.: x(x==10) = 2, will replace all x values that are currently 10 into 2

------

# Function Calls

* matrix_size = size(data)

* Create the variables x and y which respectively contain the number of rows and columns of the variable z: [x,y]= size(z)

* max function: `[xMax, idx] = max(x)` (same for min())
    * where xMax == the max value of x, idx == the index value that the max value will be assigned with
        * if you only max(a) and a is a 2D array of shape (x,y), then you will get the max value for every y column value, i.e. the shape result will be (1 , y)

* use a tilde (`~`) to ignore specific outputs

* `fft(y)`: compute the discrete Fourier transform of a vector
    * since that gives complex numbers as an output, you might want to: result = abs(fft(y)), to get the absolute value-magnitude

------

# Visualization - Plotting

* [MATLAB plot gallery documentation](https://www.mathworks.com/products/matlab/plot-gallery.html)

* Two vectors of the same length can be plotted against each other using the plot function: `plot(x,y)`
    * use log scales for each axis: `loglog(x,y)`

* `plot(x, y, "LineSpec")`, [Line Specification documentation](https://www.mathworks.com/help/matlab/ref/linespec.html) 
    * e.g., plot(x,y,"r--o") will have a red (r) dashed (--) line with a circle (o) as a marker
    
* Use line width of specific value, e.g. `plot(x, "LineWidth", 4)` will print a line width of 4. [Line Properties](https://www.mathworks.com/help/matlab/ref/matlab.graphics.chart.primitive.line-properties.html)


* use *line specification* along with *line properties*, e.g.: `plot(x,y, "ro-","LineWidth", 3)`
    * e.g. `plot(v1, v2, "ro-", "LineWidth", 4)` will plot the 2 vectors with red(r) cicle(o) markers, and the line width will be of 4

* to plot one line on top of the other type `hold on`
    *e.g.: 
        * plot(x,y,"r--o")
        * hold on
        * plot(x,z, "r*"), (red star marker)
        * hold on
        * plot(x, w, "ks") (k for black, s for square marker)
    * to exit hold on -> `hold off`

* When you plot a single vector by itself, MATLAB uses the vector values as the y-axis data and sets the x-axis data to range from 1 to n, where n is the number of elements in the vector

* descriptions
    * add title to graph: `title`("here is the plot's title")
    * x-axis description: `xlabel("here is the x-label title")`
    * y-axis description: `ylabel("here is the y-label title")`

* add **legends**: `legend(" ", " ")`

* focus on a specific area of interest in terms of range of values: `xlim([xmin , xmax])` or: xlim([xmin xmax])
    * after plot(x,y) you can use xlim for plotting specific areas of the graph

* In the right section of outputs, you can use the *output pane* to interact with specific values across the chart


* use `pause()` function to animate the plots in conjunction with using `hold on` and `hold off`, example: 
   
        for idx= 1:5 
            hold on
            plot(idx, density(idx),"*")
            hold off
            pause(0.9)
        end


------

# Programming Constructs

In MATLAB:

* if .. else .. elseif .. end (*In Python it would be if-elif-else with ":"*)

* loops:
    * for .. end

* Instead of: for i=1 .. i<=3 -->in Matlab--> for i= 1:3

* e.g. iterating through a 2D array "arr" of shape (x, 5), grabbing all column values separately and assign them to a variable called "column values"(which would be assigned 5 times since we have 5 columns): 

        for index = (1:5)
            column_values = `arr(:, index)
        end

*from the Matlab academy mathworks exercise:*

        for v= (1:7)
            s = spectra(:, v);
            if speed(v) <= 0 
                loglog(lambda,s,"--")
            else  
            loglog(lambda,s, "LineWidth", 3)
            end
            hold on
        end
        hold off
        % starnames is an array of star names in spectra
        %% otherwise it would be smth like legend("legend title")
        legend(starnames)
















-------

## Sources

[1] https://matlabacademy.mathworks.com/