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


## Test on given lists:
A = [7, 3, 6, 1, 0]
print(f"Given: {A}")
sorted_output = mergeSort(A)
print(f"Sorted output: {sorted_output}")
## Sorted output: [0, 1, 3, 6, 7]

B = [7, 6, 5, 4, 8, 3, 14, 2, 11, 1, 0, 92.75, 0.5]
print(f"Given: {B}")
sorted_output = mergeSort(B)
print(f"Sorted output: {sorted_output}")
## Sorted output: [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 11, 14, 92.75]




## DBE's Notes
""" Notes about Challenge:
    1. Implement the Quick-Sort algorithm.
        -> input:   [7, 6, 5, 4, 8, 3, 14, 2, 11, 1, 0]
        -> output:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 14]

    References:
        [1] Python 3 Documentation 
            >> https://docs.python.org/3/index.html
        [2] Merge sort - Wiki 
            >> https://en.wikipedia.org/wiki/Merge_sort
        [3] Overviews of Quick-Sort algorithm:
            1. Khan Academy
                >> https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort
            2. Merge sort algorithm by mycodeschool
                >> https://youtu.be/TzeBrDU-JaY
        [4] Thinking Recursively in Python – Real Python
            >> https://realpython.com/python-thinking-recursively/
"""


# David Booker-Earley's approach for this challenge:
    ## ** OVERVIEW **
        # 1. Accept a valid input.
        # 2. Conditionally partition input-iterable halfway (or nearly).
            # Repeat: Separate input into Left-side & Right-side.
            # Condition: Stop if sub-section has less than 2 elements.
            # An array of one (or zero) element can't be inherently unordered.
        # 3. Sort Left-side & Right-side separately.
        # 4. Build the sorted array by merging elements of each side in order.
    
    
    ## ** KEY TERMS **
        # element: fundamental ingredient of iterable
        # item: sub-section of original input-array, length may vary
            # (e.g., Left-side, Right-side)
        # N: length of array or sub-section (number of elements present)
        # partition: separate into smaller parts (i.e., split into items)
        
        # Example for clarity:
            # Consider the following list: A = [4, 0, 1]
            # Here, if A is partitioned into "Left" & "Right" sides:
                ## Inputs
                    # mid_index = len(A)//2 
                    # ... which simplifies to 3//2 and equals 1
                    # Left = A[:mid_index]
                    # Right = A[mid_index:]
                ## Outputs
                    # mid_index = 1
                    # Left = [4]
                    # ... the item "Left" has one element (N = 1)
                    # Right = [0, 1]
                    # ... the item "Right" has two elements (N = 2)
    
    
    ## ** ASSUMPTIONS **
        # 1. Array (or other iterable) contains only non-repeating numbers.
        # 2. Array is One-Dimensional of some length N.
            # (i.e., there are no nested iterables).
        # 3. When partitioning, integer-division "//" rounds down, and thus,
            # "N of Right-side" is greater than or equal to "N of Left-side".
    
    
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