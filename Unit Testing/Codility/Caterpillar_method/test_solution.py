import unittest

# import the script file to be tested
import solution_AbsDistinct

class TestSample(unittest.TestCase):

    def test_codility_example(self):
        self.assertEqual(solution_AbsDistinct.solution([-5,-3,-1,0,3,6]), 5)

    def test_Only_Negatives(self):
        self.assertEqual(solution_AbsDistinct.solution([-5,-3,-1,-2,-3,-6]), 5)
    
    def test_mix(self):
        self.assertEqual(solution_AbsDistinct.solution([-100, 99, 100, 1, 3, -3, 8, -55, 56, -99]), 7)

if __name__ == "__main__":
    unittest.main()