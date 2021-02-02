import numpy as np

# Creating a function that will go through the matrix replacing each row in order to turn it into the echelon form.
def is_Singular(a) :

    # making matrix b as a copy of a (since its values are going to be altered)
    b = np.array(a, dtype=np.float_)
    try:
        fix_row_zero(b)
        fix_row_one(b)
        fix_row_two(b)
        fix_row_three(b)
    except matrix_is_Singular:
        return True
    return False

# handling errors
class matrix_is_Singular(Exception): pass

# In the first row a[0], the 1st element a[0,0] should be equal to 1
# In the end, the row is divided by the value of a[0, 0]
def fix_row_zero(a) :

    # check if a[0,0] is equal to zero
    # if a[0,0]=0, one of the lower rows will be added to the first one before the division
    if a[0,0] == 0 :
        a[0] = a[0] + a[1]
    if a[0,0] == 0 :
        a[0] = a[0] + a[2]
    if a[0,0] == 0 :
        a[0] = a[0] + a[3]
    if a[0,0] == 0 :
        raise matrix_is_Singular()

    # divide the 1st row by the value of the 1st element a[0, 0]
    a[0] = a[0] / a[0,0]
    return a

# 2nd row
def fix_row_one(a):

    # setting the sub-diagonal elements to zero; in the 2nd row there is only the a[1,0] element
    a[1] = a[1] - a[1,0] * a[0]

    # check if the sub-diagonal element a[1,1] is equal to zero
    if a[1,1] == 0 :
        a[1] = a[1] + a[2]
        a[1] = a[1] - a[1,0] * a[0]
    if a[1,1] == 0 :
        a[1] = a[1] + a[3]
        a[1] = a[1] - a[1,0] * a[0]
    if a[1,1] == 0 :
        raise matrix_is_Singular()

    # divide the 2nd row by the value of a[1, 1]
    a[1] = a[1] / a[1,1]
    return a

# 3rd row
def fix_row_two(a) :

    # setting the sub-diagonal elements to zero, i.e. a[2,0] and a[2,1]
    a[2] = a[2] - a[2,0] * a[0]
    a[2] = a[2] - a[2,1] * a[1]
    
    # check if the sub-diagonal elements a[2,0] and a[2,1] are equal to zero
    if a[2,2] == 0 :
        a[2] = a[2] + a[3]
        a[2] = a[2] - a[2,0] * a[0]
        a[2] = a[2] - a[2,1] * a[1]
        
        a[2] = a[2] + a[3]
        a[2] = a[2] - a[1,0] * a[0]

    if a[2,2] == 0 :
        raise matrix_is_Singular()
    # setting the diagonal element to one by dividing the 3rd row by the value of a[2,2]
    a[2] = a[2] / a[2,2]
    return a

# 4th row
def fix_row_three(a) :

    # setting the sub-diagonal elements to zero, i.e. elements a[3,0], a[3,1], and a[3,2]
    a[3] = a[3] - a[3,0] * a[0]
    a[3] = a[3] - a[3,1] * a[1]
    a[3] = a[3] - a[3,2] * a[2]
    
    if a[3,3] == 0 :
        raise matrix_is_Singular()
    # Transform the row to set the diagonal element to one.
    # setting the diagonal element a[3,3] to one by dividing the 4th row by the value of a[3,3]
    a[3] = a[3] / a[3,3] 
    
    return a