# Merge Sort

## Problem Statement
Implement the Merge Sort algorithm.

>input: [7, 6, 5, 4, 8, 3, 14, 2, 11.5, 1, 0, 2]

>output: [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 11.5, 14]

## Approach
### Assumptions
1. Array (or other iterable) contains only numbers that may repeat.
1. Array is One-Dimensional of some length `N`.
    1. No nested iterables.
1. When partitioning, (floor) integer-division rounds down.
    1. Thus, `N` of _Right-side_ is greater than or equal to `N` of _Left-side_.

### Overview of Algorithm and Solution
1. **Accept** a valid _input_-iterable.
2. **Conditionally partition** _input_ halfway (or nearly).
    1. **Separate** _input_ into `Left` & `Right` sides, respectively.
    1. **Condition:** Stop if _input_ has less than 2 elements.
        - _An array of one (or zero) element can't be inherently unordered._
3. **Sort** `Left` & `Right` separately.
    1. If the length of _input_ is greater than 1, **compare** values to some reference `R`.
4. **Build** the sorted array by merging elements of each side in order.
    1. **Store or return** values based on `R`.
        - Sorted Array: [_smaller values, R, larger values_]


---


### Key Terms
* `//` = operator for (floor) integer-division
* `element` = fundamental ingredient of iterable (i.e., data value)
* `item` = sub-section of original input-array, length may vary
    * "Left-item" means "Left-side"
    * "Right-item" means "Right-side"
* `N` = length of array or sub-section (i.e., number of elements present)
* `partition` = separate into smaller parts (i.e., split into items)
* `R` = some chosen, preferred reference value
    * (e.g., some value in _Left_, _Right_, or a new _auxiliary-array_)


### Example for Clarity
Consider the following list: `A = [4, 0, 1]`

Here, `A` is partitioned into `Left` & `Right` sections using Python 3.

The `Left` item has one element (N = 1) while the `Right` item has has two elements (N = 2).

```python
>>> mid_index = len(A)//2  # which simplifies to: 3//2
>>> ## Output: 1
>>> 
>>> Left = A[:mid_index]
>>> ## Output: [4]
>>> 
>>> Right = A[mid_index:]
>>> ## Output: [0, 1]
```

---


### Solution Outline
**Apply a recursive "Divide and Conquer" approach.**
1. Accept a given array.
2. Check for invalid inputs:
    1. If valid (e.g., length is greater than 1), proceed to the "Divide and Conquer" section.
    1. If invalid, do nothing.
3. **Divide and Conquer.**
4. Print results (the sorted array).


#### Divide and Conquer Section (with code excerpts)
* _Block A, Main & Partition:_
    * If `N` of _input_ < 2: Return the current _input_.
    * If `N` of _input_ >= 2: Create a Partition-Index to split _input_ in half (or nearly).
    * Return Partition-Index to use as a bookmark.
        * `part_index = N // 2`
        * _Indices must be integers so `//` is used._
    * Store `Left` & `Right` items based on the partition.
    * Recursively call ***Block A*** on `Right` & `Left`, respectively.
    * Be sure to store each _sorted output-item_.
    * Call ***Block B*** to merge the _sorted items_.
        * Choose `Sorted Right` as an anchor, use each value as reference `R`.
        * Compare & combine _sorted items_ by placing elements of `Sorted Left` into `Sorted Right` in numerical order.
    * Return sorted-array.

* _Block B, Compare & Merge:_
    * Using a loop, compare elements `elm` of `Left` with `elm` of `Right`.
    * First, check for the _MAX-case_ & conditionally append to `Right`.
        
        ```
        If current elm of Left_item >= the last elm of Right_item: 
            Append elm to Right_item
        ```
    
    * Next, conditionally insert `elm` of `Left` into `Right`.
        
        ```
        Loop over index k, from start to N of Right_item:
            If elm of Left_item < elm of Right_item at index k:
                Insert Left elm at k inside of Right_item
                Break from current iteration of immediate loop
        ```


---

>**Remember:**
> - An item is considered to be _sorted_ if `N = 1` is **True**, or if its elements are merged in order.
> - Any `Right` item, where `N > 1` is **True**, will likely be longer than the corresponding `Left` item.
> - Thus, partition & sort any `Right` item before the `Left`, then use its values as _references_.

---


***Block B*** and ***Block A*** can be implemented in _Python 3_ like this:

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


def mergeSort(arr):
    """Block A: Main. Implements the Merge Sort algorithm.
    Input: 1-D Array of unsorted numbers.
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


## Extra Notes
### Example: Updating the Right-item with the Left-elements
The following example is a simplified process of placing every _element_ of `Left` into `Right` in order.

#### Partition
* Let's revisit the example from the **Key Terms** section.
* `mid_index` is the Partition-Index, which separates _input_ `A` into `Left` & `Right` _items_.

```python
>>> A = [4, 0, 1]
>>> mid_index = len(A)//2  # which simplifies to: 3//2
>>> ## Output: 1
>>> 
>>> Left = A[:mid_index]
>>> ## Output: [4]
>>> 
>>> Right = A[mid_index:]
>>> ## Output: [0, 1]
```


#### Merge
* Before the merger, the `Left` _item_ has one _element_ (N = 1) while the `Right` _item_ has has two _elements_ (N = 2).
* Note that each item is sorted, thus, merge `Left` elements with the `Right` item (in numerical order) using ***Block B***.
* After the merger, `Right` becomes the sorted version of _input_ `A`.

```python
>>> Right
>>> ## Output: [0, 1]
>>> 
>>> combine(Left, Right)
>>> 
>>> Right
>>> ## Output: [0, 1, 4]
```


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