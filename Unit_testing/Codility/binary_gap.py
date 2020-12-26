'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''

import unittest

def solution(N):

    bit_number = "{0:b}".format(N)

    # bit to string
    string_bit = str(bit_number)

    binary_group= False
    binary_highest=0
    binary_zero_counter = 0
    for char in string_bit:
        
        if char == "1":

            if binary_highest < binary_zero_counter:

                # aggregate the gap every time you meet a new "1"
                binary_highest = binary_zero_counter

            binary_group = True

            # re-count zeros for the next gap-group
            binary_zero_counter = 0

        elif binary_group:
            binary_zero_counter +=1

    return binary_highest


class Test_solution(unittest.TestCase):

    def test_small_negative(self):
        self.assertEqual(solution(-1), 0)
        self.assertEqual(solution(-2), 0)


    def test_large_negative(self):
        self.assertEqual(solution(-1015), 1)
        self.assertEqual(solution(-5555), 2)
        self.assertEqual(solution(-15352), 1)  

        
    def test_small_positive(self):
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(5), 1)
        self.assertEqual(solution(12), 0)
                                             
    def test_large_positive(self):
        self.assertEqual(solution(1156), 4)
        self.assertEqual(solution(5000), 3)
        self.assertEqual(solution(10586375), 5)

                  
    def test_no_gap(self):
        self.assertEqual(solution(63), 0)
        self.assertEqual(solution(64), 0)

if __name__ == '__main__':
    unittest.main()