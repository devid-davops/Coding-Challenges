# Merge Sort

## Problem Statement
Implement the Merge Sort algorithm.

>input:   [7, 6, 5, 4, 8, 3, 14, 2, 11, 1, 0]

>output:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 14]

## Approach
### Assumptions
1. Array (or other iterable) contains only numbers that may repeat.
1. Array is One-Dimensional of some length `N`.
    1. No nested iterables.
1. When partitioning, integer-division "//" rounds down.
    1. Thus, `N` of _Right-side_ is greater than or equal to `N` of _Left-side_.

### Overview of Algorithm and Solution
1. **Accept** a valid input.
2. **Conditionally partition** input-iterable halfway (or nearly).
    1. **Separate** _input_ into Left-side & Right-side.
    1. **Condition:** Stop if _input_ has less than 2 elements.
        - _An array of one (or zero) element can't be inherently unordered._
3. **Sort** Left-side & Right-side separately.
    1. If the length of _input_ is greater than 1, **compare** values to _R_.
        - Where R is some chosen, preferred reference value.
        - (e.g., some value in _Left_, _Right_, or a new _auxiliary-array_)
4. **Build** the sorted array by merging elements of each side in order.
    1. **Store or return** values based on _R_.
        - Sorted Array: _smaller values, R, larger values_


### Key Terms
* `element` = fundamental ingredient of iterable (i.e., data value)
* `item` = sub-section of original input-array, length may vary
    * _Left-item_ means "Left-side", likewise for "Right-side"
* `N` = length of array or sub-section (i.e., number of elements present)
* `partition` = separate into smaller parts (i.e., split into items)


#### Example for Clarity
Consider the following list: `A = [4, 0, 1]`

Here, `A` is partitioned into `Left` & `Right` sides using Python 3:

```python
>>> mid_index = len(A)//2  # which simplifies to 3//2
>>> ## Output: 1
>>> Left = A[:mid_index]
>>> ## Output: [4]
>>> Right = A[mid_index:]
>>> ## Output: [0, 1]
```

* The `Left` item has one element (N = 1) while the `Right` item has has two elements (N = 2).


---


> _... **NOTE:**  Updates will occur on **Oct. 18, 2019**    ~ DBE_


---


### Solution Outline
**Apply a recursive "Divide and Conquer" approach.**
1. Accept a given array.
2. Check for invalid inputs:
    1. If valid (e.g., length is greater than 1), proceed to the "Divide and Conquer" section.
    1. If invalid, do nothing.
3. **Divide and Conquer.**
4. Print results (the sorted array).


#### Divide and Conquer Section (Code Excerpts)

***Block A, Main & Partition:***

```python
def mergeSort(arr):
    """Block A: Main. Implements the Merge Sort algorithm.
    Input: 1-D Array of non-repeating numbers.
    Output: Sorted version of the input.
    """
    if len(arr) >= 2:
        # Conditionally partition input halfway (or nearly)
        part_index = len(arr)//2
        Left = arr[:part_index]
        Right = arr[part_index:]
        
        # Allow recursion on the longer item (Right-side) first
        sorted_Right = mergeSort(Right)
        sorted_Left = mergeSort(Left)
        combine(sorted_Left, sorted_Right)
        return sorted_Right
    
    else:
        return arr
```


***Block B, Sort, Compare & Merge:***

```python
def combine(Left_item, Right_item):
    """Block B: Compares elements between two items, conditionally
    merges elements of the Left item with elements of the Right item,
    and updates Right item to serve as the sorted array.
    """
    for Left_elem in Left_item:
        if Left_elem >= Right_item[-1]:
            # MAX-Case
            Right_item.append(Left_elem)
        else:
            for index_k in range(len(Right_item)):
                if Left_elem < Right_item[index_k]:
                    Right_item.insert(index_k, Left_elem)
                    break
```


> _... For more details, please see **SOLUTION** (at the bottom of this page) until updates have been made.    ~ DBE_


## Extra Notes
### Example: Updating the Right-item with the Left-elements
Recall the example from the _Key Terms_ section.

`mid_index` is the Partition-Index, which separates the input into _Left_ and _Right_ items.


```python
>>> A = [4, 0, 1]
>>> mid_index = len(A)//2  # which simplifies to 3//2
>>> ## Output: 1
>>> Left = A[:mid_index]
>>> ## Output: [4]
>>> Right = A[mid_index:]
>>> ## Output: [0, 1]
```


**Before Updating _Right_**
* The `Left` item has one element (N = 1).
* The `Right` item has has two elements (N = 2).


**After Updating _Right_**

> _... updates will illustrate how and why I update the __Right-item__ coditionally with __elements__ from the __Left-item__.    ~ DBE_



---

### Improvements (optional but possibly fun)
1. Try variations of the _merge-combine_ function.
2. Apply different case-study circumstances.
3. Account for nested iterables or empty items.


### References:
1. [Python 3 Documentation](https://docs.python.org/3/index.html)
1. [Merge sort - Wiki](https://en.wikipedia.org/wiki/Merge_sort)
1. Overviews of Merge-Sort algorithm:
    1. [Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)
    1. [Merge sort algorithm by mycodeschool](https://youtu.be/TzeBrDU-JaY)
    1. [Thinking Recursively in Python – Real Python](https://realpython.com/python-thinking-recursively/)




---

> _... I'm temporarily placing my approach here directly from my code.    ~ DBE_

---


## David Booker-Earley's approach for this challenge:
    ## ** SOLUTION **
      # Define a function that accepts a given array.
        # Check for invalid inputs:
            # IF valid: proceed (e.g., check length of input).
            # IF invalid: print "Invalid entry." or do nothing.
        
        # Divide and Conquer -> Compare each element:
            # Setup sub-function(s):
                # Block A -> Main and Partition:
                    # IF N of input >= 2: Partition input.
                        # Create a Partition-Index to split input in half:
                            # part_index = N // 2
                            # -> Indices must be integers so "//" is used.
                            # -> Input could be an array or item.
                        # Return Partition-Index to use as a bookmark.
                        # Store "Left" and "Right" items from partition.
                        # Recursively call main on Right-side of bookmark.
                            # Store sorted output.
                                # -> Any Right item with N > 1 will likely be
                                # -> longer than the corresponding Left item,
                                # -> thus, process each Right item first.
                        # Recursively call main on Left-side of bookmark.
                            # Store sorted output.
                        # Call Block B to Merge:
                            # Combine Sorted-Left & Sorted-Right in order.
                        # Return sorted-array.
                    # ELSE:
                        # IF N < 2:
                            # Return the current input
                
                # Block B -> Compare and Merge:
                    # Compare element(s) of item Left with those of Right.
                    # Conditionally append or insert Left-element into Right:
                    # -> "Right" is already sorted (via function or "N = 1").
                        # for every element (elm) inside Left:
                            # IF current elm in Left >= the last elm in Right:
                                # Do MAX-case: append Left-elm to Right-item.
                            # ELSE Loop over index k from start to N of Right:
                                # if Left-elm is < Right-elm at index k:
                                    # insert Left-elm at k
                                    # Break from current loop-iteration      
      
      # Call mergeSort() on a given list and store the sorted output.
      # Print results.
    
    
    ## ** IMPROVEMENTS (Extra Practice for Fun) **
        # 1. Try variations of the "merge" or "combine" function.
        # 2. Apply different case-study circumstances.
        # 3. Account for nested iterables or empty items.
    
    
    ## Notes to self for Testing and Troubleshooting:
        # Take time to conceptually go through each block of code.
        # Track how the loops occur.
        # Track inputs & outputs.
        # Be sure the code & its action match conceptual approach.