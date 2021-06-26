'''
An array A consisting of N integers is given. An inversion is a pair of indexes (P, Q) such that P < Q and A[Q] < A[P].

Write a function:

def solution(A)

that computes the number of inversions in A, or returns −1 if it exceeds 1,000,000,000.

For example, in the following array:

 A[0] = -1 A[1] = 6 A[2] = 3
 A[3] =  4 A[4] = 7 A[5] = 4
there are four inversions:

   (1,2)  (1,3)  (1,5)  (4,5)
so the function should return 4.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''

def solution(A): 
  
    inv_count = 0
    for i in range(len(A)): 
        for j in range(i + 1, len(A)): 
            if (A[i] > A[j]): 
                inv_count += 1

    if inv_count > 1000000000:
        return -1
    else:
        return inv_count 


# testing
import unittest

class Test_Inv_Count(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([-1,6,3,4,7,4]), 4)

        self.assertEqual(solution([4,3,10,15,20,25]), 1)
    
if __name__ == "__main__":
    unittest.main()