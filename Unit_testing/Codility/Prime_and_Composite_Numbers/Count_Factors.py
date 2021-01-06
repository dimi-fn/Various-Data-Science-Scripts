'''
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''

def solution_1(n):

    factors=[]

    for i in range (1,(n+1)):
        if n%i==0:
            factors.append(i)

    return len(factors)

'''
Although the above solutions catches 100% correctness on Codility, however it has 57% total result because of timeout errors and time performance
'''

import math
from math import sqrt

def solution_2(n): 

    # to set, to avoid duplicates
    factors= set()

    for i in range(1, int(math.sqrt(n))+1):
        if n % i ==0:
            factors.add(i)
            factors.add(int(n/i))
    
    numbers_of_factors= len(factors)
    return numbers_of_factors


# Testing
import unittest

class Test_solution(unittest.TestCase):
    
    def test_solution_1(self):

        # factors of 24: [1,2,3,4,6,8,12,24] --> 8 factors
        self.assertEqual(solution_1([24]), 5)

        # factors of 75: [3,5,15,25,75] --> 5 factors
        self.assertEqual(solution_1([75]), 5)

    def test_solution_2(self):

        # factors of 24: [1,2,3,4,6,8,12,24] --> 8 factors
        self.assertEqual(solution_2([24]), 5)

        # factors of 75: [3,5,15,25,75] --> 5 factors
        self.assertEqual(solution_2([75]), 5)

        
if __name__ == "__main__":
    unittest.main()