'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''

def solution(A):
    n = len(A)+1
    total = n*(n+1)//2
    sum_of_A = sum(A)
    return total - sum_of_A

import unittest

class Test_solution(unittest.TestCase):

    def test_missing(self):
        self.assertEqual(solution([2,3,1,5]), 4)
        self.assertEqual(solution([1,2,3,5]), 4)
        self.assertEqual(solution([1,8,5,6,7,3,4]), 2)


if __name__ == "__main__":
    unittest.main()