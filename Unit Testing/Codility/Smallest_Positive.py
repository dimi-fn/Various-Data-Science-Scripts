'''
Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−1,000,000..1,000,000]
'''

import unittest

def solution(x):

    # return 1 in the following cases:
    if max(x) <= 0 or (max(x)==2 and min(x)!=1):
        return 1

    else:
      # If nothing of the above occurs then: sort the list and keep only the positive numbers
      x.sort()
      sorted_positive_list = [num for num in x if num>0]

      if min(sorted_positive_list) != 1:
          return 1
      else:
          '''
          - Find the 1st occurrence of the pair of integers where the difference is greater than 2,
          and then return the smallest positive number that does not exist in the list,
          e.g. if x= [1,2,3,5] then return 4
          - Else, return the max plus one,
          e.g. if x=[1,2,3], then return 4
          '''
          for i in range(len(sorted_positive_list)-1):
              difference = sorted_positive_list[i+1] - sorted_positive_list[i]
              if difference >=2:
                  return sorted_positive_list[i] + 1
          return max(sorted_positive_list)+1
          
# Testing:
class Test_solution(unittest.TestCase):

    def test_case_one_negative(self):

        # with 3 lines
        given_input = [-10]
        validation= solution(given_input)
        self.assertEqual(validation, 1)

        # with 2 lines
        validation = solution([-10])
        self.assertEqual(validation, 1)

        # with 1 line
        self.assertEqual(solution([-10]), 1)

    def test_case_negatives(self):
        self.assertEqual(solution([-111,-222,-333]), 1)
        self.assertEqual(solution([-555,-666,-777]), 1)
        self.assertEqual(solution([-800,-900,-657]), 1)

    def test_case_negatives_zero(self):
        self.assertEqual(solution([-5,-3,0]), 1)
        self.assertEqual(solution([-10,0,-26]), 1)
        self.assertEqual(solution([0,-5,-2]), 1)
    
    def test_case_single_positiveOne(self):
        self.assertEqual(solution([1]), 2)

    def test_case_One_Two(self):
        self.assertEqual(solution([1,2]), 3)

    def test_case_mix(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(solution([1, 2, 3]), 4)
        self.assertEqual(solution([7,-5,-2]), 1)
        self.assertEqual(solution([-3,15,-6]), 1)
        self.assertEqual(solution([0,-63,89]), 1)
        

    def test_case_large_number_mix(self):
        self.assertEqual(solution([1, 2, 20569, 654795, 6560662]), 3)
        self.assertEqual(solution([5659595, 65959595, 5959, 959, 59989875]), 1)
        self.assertEqual(solution([10015444, 6594162, 6649, 959877896]), 1)

if __name__ == "__main__":
    unittest.main()