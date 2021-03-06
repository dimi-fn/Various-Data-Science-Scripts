# Unit Testing

## Contents

* [Codility](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Unit%20Testing#codility)
* [CodinGame](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Unit%20Testing#codingame)
* [Operations](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Unit%20Testing#operations)
* Miscellaneous on Testing
    * [End-to-End Testing](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Unit%20Testing#end-to-end-testing)
* [Useful Sources](#useful-sources)    

-----

## Codility

Several taks to be solved provided by [Codility](https://app.codility.com/programmers/) via unit testing. The problem details are described inside the respective subfolders and coding solutions.

* [Smallest_Positive_Number.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Smallest_Positive.py):  The smallest positive number which is not appeared in an array of numbers [[1](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Unit-Testing), [2](https://stackoverflow.com/questions/51719848/find-the-smallest-positive-integer-that-does-not-occur-in-a-given-sequence)].


* [Password_Validation.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Password_Validation.py): Creating a function for password validation.

Subfolders: 

### Iterations
* [binary_gap.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Iterations/Binary_gap.py): Find longest sequence of zeros in binary representation of an integer [[3](https://markpetherbridge.co.uk/blog/codility-binary-gap-positive-integer-solution/),[4](https://github.com/mgoldsmith1/Codility/blob/master/binaryGap.py)].             


### Arrays
* [Arrays_Cyclic_Rotation.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Arrays/Arrays_Cyclic_Rotation.py): Rotate an array to the right by a given number of steps [[5](https://medium.com/@sichangpark/codility-2-2-arrays-cyclicrotation-4215350decb1),[6](https://gist.github.com/NicholusMuwonge/b4792af7f592c171a901d1a21560e6c0)].       

* [Odd_Occurrences_in_Array.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Arrays/Odd_Occurrences_in_Array.py): Find value that occurs in odd numbers of elements [[7]](https://medium.com/@sichangpark/codility-2-1-arrays-oddoccurrencesinarray-cf4c1f7d7caf).

### Time Complexity

* [Perm_Missing_Element.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Time_Complexity/Perm_Missing_Element.py): Find the missing element in a given permutation.

* [permutation_check.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Counting_Elements/permutation_check.py): Check whether array A is a permutation [[8]](https://stackoverflow.com/questions/28178460/increasing-code-performance-of-codility).

### Prefix Sums

* [Prefix_sums.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Prefix_sums/Prefix_sums.py): Count the number of passing cars on the road [[9]](https://stackoverflow.com/questions/23774985/codility-passing-car?page=1&tab=votes#tab-top).        

### Sorting

[distinct.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Sorting/distinct.py): Compute number of distinct values in an array.

### Leader

[dominator.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Leader/dominator.py): Find an index of an array such that its value occurs at more than half of indices in the array.

### Maximum Slice Problem

[Max_Profit.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Maximum_Slice_Problem/Max_Profit.py): Given a log of stock prices compute the maximum possible earning.

### Prime & Composite Numbers

[Count_Factors.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Prime_and_Composite_Numbers/Count_Factors.py): Count factors of given number n [[10](https://www.tutorialspoint.com/How-to-Find-Factors-of-Number-using-Python),[11](https://www.mathsisfun.com/prime-composite-number.html),[12](
    https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python#answer-6800214)].
    

### Caterpillar method

[Number of Distinct Absolute Values](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Unit%20Testing/Codility/Caterpillar_method): Compute number of distinct absolute values of sorted array elements.

### Tasks from Indeed Prime 2016 College Coders Challenge

[tennis_tournament.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Tasks_from_Indeed_Prime_2016_College_Coders_Challenge/tennis_tournament.py): Given the numbers of players and available courts, calculate the maximum number of parallel tennis games.

### Future Training
[Array_Inversion_Count.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/Codility/Future_Training/Array_Inversion_Count.py): Compute number of inversion in an array [[13](https://www.geeksforgeeks.org/counting-inversions/)].


------

## CodinGame

* [The_Descent.py](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Unit%20Testing/CodinGame/The%20Descent/The_Descent.py): a game for loops.

-----

## Operations:

Testing that any two given numbers will give the right result for the operations of addition, subtraction, multiplication, and division via Unit Testing.
* _"unit_test_sample.py"_ contains the sample to be tested, the testing of which is conducted via Unit Testing in the _"test_sample.py"_ file.
* Thus, a total number of 4 tests are conducted, with 3 testing methods for each case except for the division case where one more method is added for checking the occurrence of dividing with zero.

<br>

`if __name__ == '__main__':`

* when a program is executed directly, the variable `name` is defined as `main` by default.
* when it is imported as a module, the value of name is the name of the module.

----

## Miscellaneous on Testing

### End-to-End Testing

https://www.freecodecamp.org/news/end-to-end-testing-tutorial/?fbclid=IwAR0AjhwTRBkptLtO0CNo4pk6LkanYfCkvFTNPvhLDvQLxDdQTwNMJYmIjHQ

---------

# Useful Sources

[1] https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Unit-Testing

[2] https://stackoverflow.com/questions/51719848/find-the-smallest-positive-integer-that-does-not-occur-in-a-given-sequence

[3] https://markpetherbridge.co.uk/blog/codility-binary-gap-positive-integer-solution/

[4] https://github.com/mgoldsmith1/Codility/blob/master/binaryGap.py

[5] https://medium.com/@sichangpark/codility-2-2-arrays-cyclicrotation-4215350decb1

[6] https://gist.github.com/NicholusMuwonge/b4792af7f592c171a901d1a21560e6c0)

[7] https://medium.com/@sichangpark/codility-2-1-arrays-oddoccurrencesinarray-cf4c1f7d7caf

[8] https://stackoverflow.com/questions/28178460/increasing-code-performance-of-codility

[9] https://stackoverflow.com/questions/23774985/codility-passing-car?page=1&tab=votes#tab-top

[10] https://www.tutorialspoint.com/How-to-Find-Factors-of-Number-using-Python

[11] https://www.mathsisfun.com/prime-composite-number.html

[12] https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python#answer-6800214

[13] https://www.geeksforgeeks.org/counting-inversions/

[14] https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

[15] https://www.freecodecamp.org/news/end-to-end-testing-tutorial/?fbclid=IwAR0AjhwTRBkptLtO0CNo4pk6LkanYfCkvFTNPvhLDvQLxDdQTwNMJYmIjHQ