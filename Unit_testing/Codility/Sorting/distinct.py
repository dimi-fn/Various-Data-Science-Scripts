'''
Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):

    distinct_list = list(set(A))

    count=0
    for unique_num in distinct_list:  #pylint: disable=unused-variable
        count+=1
    return count


# Testing:
import unittest

class Test_solution(unittest.TestCase):

    def test_distinct(self):
        
        self.assertEqual(solution([2,1,1,2,3,1]), 3)
        self.assertEqual(solution([10,11,11,12,12,13,14,15,15,16,16]), 7)
        self.assertEqual(solution([1000,1000,1010,1010,1111,1111]), 3)

if __name__ == "__main__":
    unittest.main()