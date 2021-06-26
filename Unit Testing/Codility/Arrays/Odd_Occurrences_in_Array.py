'''
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
'''
import unittest

def solution (N):

    # dictionary storing the number and its frequency value from the N array
    dict_numbers_occurr = {}

    # storing the frequency of each element
    count_frequency = 0

    for num in N:

        count_frequency+=1
        dict_numbers_occurr[num] = N.count(num)

        for num, frequency_value in dict_numbers_occurr.items():

            # if the corresponding key value is odd number -> this number is the unpaired element
            if frequency_value % 2 ==1:
                return num

'''
Although the above solution can be generalized for unlimited pairs of elements (e.g. N= [1,1,1,1,2,2,3,3,3,4] and not just N=[1,1,2,2,3,3,4]), 
it faces time performance issues when a very long array is given.

Therefore, another solution can be as followed:
'''

def solution_2(N):     

    if len(N) == 1:
         return N[0]

    N = sorted(N) 
    for i in range(0 , len (N) , 2): 
         if i+1 == len(N):
             return N[i]
         if N[i] != N[i+1]:
             return N[i]

# Testing:
class Test_solution(unittest.TestCase):

    def test_array(self):
        self.assertEqual(solution([1, 1, 2, 2, 3, 3, 4]), 4)
        self.assertEqual(solution([1, 1, 2, 2, 3, 3, 4, 4, 5]), 5)
        self.assertEqual(solution([30, 30, 40, 40, 50, 50, 60]), 60)
        self.assertEqual(solution([122, 122, 166, 166, 188, 188, 188, 190, 190]), 188)

    def test_array_2(self):
        self.assertEqual(solution_2([1, 1, 2, 2, 3, 3, 4]), 4)
        self.assertEqual(solution_2([1, 1, 2, 2, 3, 3, 4, 4, 5]), 5)
        self.assertEqual(solution_2([30, 30, 40, 40, 50, 50, 60]), 60)
        self.assertEqual(solution_2([122, 122, 166, 166, 188, 188, 188, 190, 190]), 188)


if __name__ == "__main__":
    unittest.main()