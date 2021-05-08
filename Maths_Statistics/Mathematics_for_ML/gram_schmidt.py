import numpy as np
import numpy.linalg as la

small_number= 1e-14 

def gram_schmidt_basis(A):

    # set B as a copy of A, since its values are going to be altered
    B = np.array(A, dtype=np.float_) 

    # looping over the vectors, starting with zero, label them with i
    for i in range(B.shape[1]) :

        # Inside the above loop, looping all previous j vectors to substract
        for j in range(i):

            # Substracting the overlap with previous vectors using the corresponding dot product
            # current vector is B[:, i], previous vector is B[:, j]
            B[:, i] = B[:,i] - B[:,i] @ B[:,j] * B[:,j]

        # normalisation test for B[:, i]
        if la.norm(B[:, i]) > small_number:
            B[:, i] = B[:, i] / la.norm(B[:, i])  
        else :
            B[:, i] = np.zeros_like(B[:, i])      
            
    # returning the result
    return B

# using the Gram-schmidt process to calculate the dimension spanned by a list of vectors
# the sum of all the norms will be the final number of dimensions (since each vector is normalized to 1 or 0)
def calc_dimensions(A):
    return np.sum(la.norm(gram_schmidt_basis(A), axis=0))

# test the function
vector_v = np.array([[1,0,2,6],
                    [0,1,8,2],
                    [2,8,3,1],
                    [1,-6,2,3]], dtype=np.float_)

gram_schmidt_basis(vector_v)

# find number of dimensions of "vector_v"
calc_dimensions(vector_v)