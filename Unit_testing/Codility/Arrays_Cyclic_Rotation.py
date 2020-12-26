'''
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [-1,000..1,000].
'''

import unittest

def solution(A, K):
    
    number_of_rotations = K
    iteration_count = 0
    while A != []:
      while number_of_rotations>0:

          # Shift the last element of the array to the first place 
          A.insert(0, A[len(A)-1])

          # And then delete the shifted element from the previous position
          del(A[len(A)-1])
          iteration_count+=1

          if iteration_count == number_of_rotations:

              # break when iteration_count==K
              break
      return A
    else:
        return []


class Test_solution(unittest.TestCase):

    def test_small_negative(self):
        
        self.assertEqual(solution([3, 8, 9, 7, 6] , 1), [6, 3, 8, 9, 7])

        self.assertEqual(solution([3, 8, 9, 7, 6] , 2), [7, 6, 3, 8, 9])

        self.assertEqual(solution([3, 8, 9, 7, 6] , 3), [9, 7, 6, 3, 8])


if __name__ == '__main__':
    unittest.main()