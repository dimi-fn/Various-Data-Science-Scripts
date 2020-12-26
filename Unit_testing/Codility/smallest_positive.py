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
        given_input = [-10]
        validation= solution(given_input)
        self.assertEqual(validation, 1)

    def test_case_negatives(self):
        given_input = [-100, -5]
        validation= solution(given_input)
        self.assertEqual(validation, 1)

    def test_case_negatives_zero(self):
        given_input = [-133, -52, 0]
        validation= solution(given_input)
        self.assertEqual(validation, 1)
    
    def test_case_single_positiveOne(self):
        given_input = [1]
        validation= solution(given_input)
        self.assertEqual(validation, 2)

    def test_case_One_Two(self):
        given_input = [1, 2]
        validation= solution(given_input)
        self.assertEqual(validation, 3)

    def test_case_postives_negatives(self):
        given_input = [-10, 3, 6, 4, 1, 2]
        validation= solution(given_input)
        self.assertEqual(validation, 5)

    def test_case_large_number_mix(self):
        given_input = [-1, 3000, 6000, 4000, 1000, 2000]
        validation= solution(given_input)
        self.assertEqual(validation, 1)

if __name__ == "__main__":
    unittest.main()