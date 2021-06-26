'''
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
'''

def solution(A):

    if len(A) ==1:
        return 0
    else:
        # if there is repetition of number(s) then it is not permutation
        if len(list(set(A))) != len(A):
            return 0
        else:
            A = list(set(A))
            my_list=[]
            for i in range(len(A)-1):
                difference = A[i+1] - A[i]
                my_list.append(difference)

            if sum(my_list)+1 == len(A):
                return 1
            else:
                return 0

# Testing:
import unittest

class Test_solution(unittest.TestCase):

    def test_permutation(self):
        self.assertEqual(solution([1,2,4,3]), 1)
        self.assertEqual(solution([1,2,4]), 0)
        self.assertEqual(solution([1,2,3,4,4]), 0)
        self.assertEqual(solution([10,11,12,12,14,13]), 0)
        self.assertEqual(solution([10,11,12,14,13]), 1)
        self.assertEqual(solution([10]), 0)

if __name__ == "__main__":
    unittest.main()