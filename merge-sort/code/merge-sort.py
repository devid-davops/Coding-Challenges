# Block of code


# Block of code


# Call main on given lists:














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
"""


# David Booker-Earley's approach for this challenge:
    ## ** OVERVIEW **
        # 1. Accept a valid input.
        # 2. Conditionally partition iterable halfway (or nearly).
            # Repeat: Separate input into Left-side & Right-side.
            # Condition: Stop if sub-section has less than 2 elements.
            # An array of one (or zero) element can't be inherently unordered.
        # 3. Sort Left-side & Right-side separately.
        # 4. Build the sorted array by merging elements of each side in order.
    
    
    ## ** KEY TERMS **
        # element: fundamental ingredient of iterable
        # item: sub-section of original input-array, length may vary
            # (i.g., Left-side, Right-side)
        # N: length of array or sub-section (number of elements present)
        # partition: separate into smaller parts (i.e., split into items)
        
        # Example for clarity:
            # Consider the following list: A = [4, 0, 1]
            # Here, if A is partitioned into "Left" & "Right" sides:
                # Left = [4]
                # ... the item "Left" has one element (N = 1)
                # Right = [0, 1]
                # ... the item "Right" has two elements (N = 2)
    
    
    ## ** ASSUMPTIONS **
        # 1. Array (or other iterable) contains only non-repeating numbers.
        # 2. Array is One-Dimensional of some length N.
            # (i.e., there are no nested iterables).
        # 3. When partitioning, integer-division rounds down, and thus,
            # "N of Right-side" is greater than or equal to "N of Left-side".
    
    
    ## ** SOLUTION **
      # Define a function that accepts a given array along with "start-index"
      # -> and "end-index", these section boundaries are needed to proces the
      # -> array & its sub-sections:
        # Check for invalid inputs:
            # IF valid: proceed.
            # IF invalid: print "Invalid entry." or do nothing.
        
        # Divide and Conquer -> Compare each element:
            # Setup sub-function(s):
                # Block A -> Main and Partition:
                    # Partition Code-BLock
                        # ... partition only if N >= 2
                        # ... return Partition-Index as a bookmark
                    # Recursive call on Left-side of bookmark
                    # Recursive call on Right-side of bookmark
                
                # Block B -> Compare and Merge:
                    # Compare element(s) of item "Left" with those of "Right".
                    # Conditionally append or insert Left-element into Right.
                    # -> "Right" is already sorted (via function or "N = 1").
                        # for every element (elm) inside Left:
                            # IF current elm in Left >= the last elm in Right:
                                # Do MAX-case: append Left-elm to Right-item.
                            # ELSE Loop over index k from start to N of Right:
                                # if Left-elm is < Right-elm at index k:
                                    # insert Left-elm at k, increment k by 1.
      
      
      
      # Test on given lists: 
        # [7, 3, 6, 1, 0]
        # [7, 6, 5, 4, 8, 3, 14, 2, 11, 1, 0]
      # Call mergeSort() on given list using "start-index = 0" with "end-index = len(array) - 1"
      # Print results.
    
    
    ## ** IMPROVEMENTS (Extra Practice for Fun) **
        # 1. Try variations of the "merge" or "combine" function.
        # 2. Apply different case-study circumstances.
    
    
    ## Notes to self for Testing and Troubleshooting:
        # Take time to conceptually go through each block of code.
        # Track how the loops occur.
        # Track inputs & outputs.
        # Be sure the code & its action match conceptual approach.