'''
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
'''

def solution(A):

    revenues_all_combinations = []

    max_difference_days = len(A)-1

    difference_day = 1

    while difference_day <= max_difference_days:
        
        for i in range (difference_day, len(A)):

            if A[i] > 0:
                difference = A[i] - A[i-difference_day]
                revenues_all_combinations.append(difference)           
        difference_day+=1

    if len(revenues_all_combinations)==0 or max(revenues_all_combinations) <=0:
        return 0
    else: 
        return max(revenues_all_combinations)


# Testing
import unittest

class Test_solution(unittest.TestCase):
    
    def test_profit(self):

        # 1500-900 = 600 = max profit
        self.assertEqual(solution([1000, 900, 1200, 1500, 800]), 600)

        # 50 - 10 = 40 = max profit
        self.assertEqual(solution([25, 10, 35, 23, 50]), 40)
    
    def test_loss(self):
        self.assertEqual(solution([25, 10, 9, 8, 5]), 0)
        self.assertEqual(solution([25, -10, -9, -8, 0]), 0)
        
if __name__ == "__main__":
    unittest.main()