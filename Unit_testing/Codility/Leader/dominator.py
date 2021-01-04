'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return -1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [-2,147,483,648..2,147,483,647].
'''

from collections import Counter

def solution(A):

    # finding the numbers and its frequency values
    sorted_counting_elemenents = Counter(A).most_common()

    # the 1st pair of elements in the above list contains the dominator number and its frequency value
    # therefore below choosing that first pair
    potential_dominator = sorted_counting_elemenents[0]

    # the dominator
    dominator= potential_dominator[0]   

    # the dominator's frequency
    frequency_of_dominator = potential_dominator[1]

    # if dominator appears less than half of the total number of elements in A or if
    # array A is empty => return -1
    #  otherwise return one of the dominator's indices
    if frequency_of_dominator <= (len(A)/2) or len(A)==0 :
        return -1

    # return 0 if array has only one element (index=0)
    elif len(A)==1:
        return 0
    else:
        for index, num in enumerate(A):
            if num == dominator:
                # this will return the index of the 1st dominant's occurence
                return index 

import unittest 
class Test_solution(unittest.TestCase):
    '''
    if array A has a dominator, then based on the function solution, the first index
    of the dominant number appearance should be returned, otherwise -1
    '''
    def test_dominator(self):

        self.assertEqual(solution([3,4,3,2,3,-1,3,3]), 0)

        self.assertEqual(solution([4,3,3,2,3,-1,3,3]), 1)

        self.assertEqual(solution([1,2,3,4,5,6,7,7,7,7,7,7,7]), 6)

    def test_non_dominator(self):

        self.assertEqual(solution([4,2,3,2,3,-1,3,15]), -1)

        self.assertEqual(solution([1,2,3,4,5,6,7,7,7,7]), -1)

if __name__ == "__main__":
    unittest.main()