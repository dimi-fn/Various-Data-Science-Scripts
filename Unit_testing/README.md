Two tests are conducted here:

1) Testing that any two given numbers will give the right result for the operations of addition, subtraction, multiplication, and division via Unit Testing.
* _"unit_test_sample.py"_ contains the sample to be tested, the testing of which is conducted via Unit Testing in the _"test_sample.py"_ file.
* Thus, a total number of 4 tests are conducted, with 3 testing methods for each case except for the division case where one more method is added for checking the occurrence of dividing with zero.

2) A task to be solved provided by [Codility](https://app.codility.com/programmers/), describing as followed:

Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−1,000,000..1,000,000]