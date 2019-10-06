# Quick Sort

## Problem Statement
Implement the Quick Sort algorithm.
>input:   [7,6,5,4,3,2,1,0]
>output:  [0,1,2,3,4,5,6,7]

## Approach
### Assumptions
1. Array (or other iterable) contains only numbers.
2. Array is One-Dimensional of length N (i.e., there are no nested iterables).
3. Array contains mostly distinct, non-repeating numbers.
4. A pivot-selection (reference-value) of the last (i.e., right-most) array-element is sufficient.

### Overview of Algorithm and Solution
1. **Select a Pivot.**
    1. Set a reference-value (pivot).
1. **Partition the given array.**
    1. Set a partition-index (PI) to separate the iterable into sections (values on the “left” and values on the “right”).
1. **Compare each value in iterable and move:**
    1. Move “less-than-pivot” values to the left of PI.
    1. Move “greater-than-pivot” values to the right of PI.
1. **Repeat** all steps for the left and right sides, respectively, until a condition is met.
    1. **Condition:** Stop breaking into smaller sections when the current sub-section has less than two elements.

---

### Solution Outline
**Apply a recursive "Divide and Conquer" approach.**
1. Accept a given array along with a "start-index" and an "end-index" (the section-view boundaries).
2. Check for invalid inputs:
    1. If valid (i.g., length is greater than 1), proceed to the "Divide and Conquer" section.
    1. If invalid, do nothing.
3. **Divide and Conquer.**
4. Print results.


#### Divide and Conquer Section
* *Block A, Main:*
  * Accept and apply section-view boundaries on given array.
  * Check if "start" is less than "end" to ensure program will work from left to right.
  * If "start" is less than "end": Call *Block B* to partition the array, and use the PI as a bookmark.
  * Apply Recursion of main to process each section of array (Left side of PI, and Right side of PI).
  * Stop recursion (do nothing) if there is one element or less in current section.
* *Block B, Partition:*
  * Accept an array and section-view boundaries.
  * Set the **Pivot** (reference-value) to the last element in the array.
  * Set the _Partition-Index (PI)_ to the first element in the array.
  * Compare the **Pivot** to each item in the array, but don't compare it to itself (compare in a _loop_ from "start" to "end - 1").
  * If the value at index **_i_** (i.g., _array[i]_) is less than or equal to the **Pivot's** value, swap the value at **_i_** with the value at the _PI_, and then increment the _PI_ by one to move linearly from left to right to the next item in the array.
  * After exiting the loop, swap the value at the _PI_ with the value at the **Pivot**.
  * Return the actual Partition-Index (index, not value) to allow recursion.


## Extra Notes

### Improvements (optional but possibly fun)
1. Try variations of the "partition" function.
2. Test other pivot selections, like the "Median-of-three" rule, and apply different case-study circumstances.
3. Should the program account for various array-types?


### References:
1. [Python 3 Documentation](https://docs.python.org/3/index.html)
1. [Quicksort Wiki](https://en.wikipedia.org/wiki/Quicksort#Implementation_issues)
1. Overviews of Quick-Sort algorithm:
    1. [Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort)
    1. [Quicksort algorithm by mycodeschool](https://youtu.be/COk73cpQbFQ)