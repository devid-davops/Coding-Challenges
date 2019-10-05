def partition(arr, start_index, end_index):
    """# Block B -> Partitions a given iterable using index-boundaries. Sorts numbers (least to greatest) using Partition-Index, PI. Returns PI."""
    ref_val = arr[end_index] # set reference-value to the last value in array, use "end-index" input rather than "-1" to be consistent and robust.
    part_indx = start_index
    for i in range(start_index, end_index): # iterate via index from start (inclusive) to end (exclusive: "end - 1")
        if arr[i] <= ref_val:
            arr[i], arr[part_indx] = arr[part_indx], arr[i] # update array: swap values to separate "less" from "greater"
            part_indx += 1
    # Swap values: a) last array-element and b) value at Partition-Index
    arr[end_index], arr[part_indx] = arr[part_indx], arr[end_index] # update array and its bookmark
    return part_indx


def quickSort(arr, start_index, end_index):
    """# Block A -> Main. Implement the Quick Sort algorithm for a given array using 'start' and 'end' indices as partition boundaries."""
    # Check for valid inputs:
    # - "Divide and Conquer" approach should occur recursively if length of sectioned-array is greater than 1,
    # - and if 'start-index' is less than 'end-index' (based on Left to Right approach).
    if len(arr) > 1:
        if start_index < end_index: # separate check-lines for easier Troubleshooting
            partition_index = partition(arr, start_index, end_index) # call Block B to separate values & return the bookmark PI
            quickSort(arr, start_index, partition_index - 1) # recursively process left side of PI
            quickSort(arr, partition_index + 1, end_index) # recursively process right side of PI


# Call main on given lists:
given = [2,7,1,4]
print(f"Given: {given}")
quickSort(given, 0, len(given) - 1)
print(f"Sorted: {given}")

given = [7,6,5,4,3,22,1,0,9,2]
print(f"Given: {given}")
quickSort(given, 0, len(given) - 1)
print(f"Sorted: {given}")

given = list(range(0,9))
print(f"Given: {given}")
quickSort(given, 0, len(given) - 1)
print(f"Sorted: {given}")




## DBE's Notes
""" Notes about Challenge:
    1. Implement the Quick-Sort algorithm.
        -> input:   [7,6,5,4,3,2,1,0]
        -> output:  [0,1,2,3,4,5,6,7]

    References:
        [1] Python 3 Documentation 
            >> https://docs.python.org/3/index.html
        [2] Quicksort - Wiki 
            >> https://en.wikipedia.org/wiki/Quicksort#Implementation_issues
        [3] Overviews of Quick-Sort algorithm:
            1. Khan Academy
                >> https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort
            2. Quicksort algorithm by mycodeschool
                >> https://youtu.be/COk73cpQbFQ
"""


# David Booker-Earley's approach for this challenge:
    ## ** ASSUMPTIONS **
        # 1. Array (or other iterable) contains only numbers.
        # 2. Array is One-Dimensional of length N 
            # (i.e., there are no nested iterables).
        # 3. Array contains mostly distinct, non-repeating numbers.
        # 4. A pivot-selection (reference-value) of the last
            # (i.e., right-most) array-element is sufficient.
    
    
    ## ** SOLUTION **
    # Define a function that accepts a given array along with "start-index"
    # and "end-index" (section boundaries for processing array):
        # Check for invalid inputs:
            # if valid (length is greater than 1): proceed.
            # if invalid: print "Invalid entry." or do nothing.
        
        # Divide and Conquer -> swap elements to avoid memory allocation of more arrays:
            # Setup sub-function(s):
                # Block A -> Main:
                    # Accpet indices as section boundaries to apply while processing array: "start-index" and "end-index".
                    # Check if "start" is less than "end" to ensure program will work from left to right.
                    # if start < end:
                        # Partition (divide into parts) the array using inputs: array, start-index, end-index. Use a PI as a bookmark.
                            # Call Block B to Partition and process each section of the array, which should allow recursion (function calling itself).
                            # ... ... Block B should separate values that are greater than a reference-value value from values that are less than that ref_val value,
                            # ... ... and then return the bookmark or Partition-Index (PI) at which the values are separated.
                        # Apply Recursion of main to process each section of array based on a condition:
                            # Condition for recursion: 
                                # Stop recursion (do nothing) if length of sectioned-array is 0 or 1 (stop if there is only one element in current section).
                                # "Divide and Conquer" if length of sectioned-array is greater than 1 (just like the initial check for invalid inputs).
                                    # LEFT SIDE of PI:
                                        # Pass "array, start-index, PI - 1" as the inputs (array, start-index, end-index) into main.
                                        # ... Notice that "PI - 1" is needed to continue the process of breaking into sections on the LEFT until condition is met.
                                    # RIGHT SIDE of PI:
                                        # Pass "array, PI + 1, end-index"
                                        # ... Notice that "PI + 1" is needed for the RIGHT side of the PI-bookmark.
                    ## maybe add an "else" to print("'start-index' must be less than 'end-index'").
                
                # Block B -> Partition, Move Index Linearly from Left to Right:
                    # Accept: array, start (the start-index), end (the end-index)
                    # Set the last element in the given sectioned-array (array[end-index]) as the current reference-value (ref_val).
                    # Set the first element as a Partition-Index (PI = start) to serve as a divider between values greater than and less than the value at ref_val.
                    # Compare each item of iterable (array) to the ref_val, but don't compare the ref_val to itself.
                        # for index_i from "start" to "end - 1":
                        # ... if value at index "i" (array[i]) is less than or equal to the ref_val's value, "swap" the value at array[i] with the value at the PI.
                        # ... ... in python, I can swap objects using tuple syntax like this: "a, b = b, a".
                        # ... ... increment PI by one after swapping its value.
                    # After the loop (outside loop), swap the value at PI with the value at ref_val.
                    # Return the actual Partition-Index (index, not value) to allow recursion.
                
                ## No need to call "return array" because the array itself is being manipulated.
                ## A better way to implement "Do Nothing" condition-statements:
                    ## When we want the code to "do nothing for case a < b", avoid extra non-essential code, 
                    ## ... if possible, simply make code "do something for case a > b" ... thus, no need for "elif-else: do nothing".
    ##
    # Test on given list: [7,6,5,4,3,2,1,0]
    # Call quickSort() on given list using "start-index = 0" with "end-index = len(array) - 1"
    # Print results.
    
    
    ## ** IMPROVEMENTS (Extra Practice for Fun) **
        # 1. Try variations of the "partition" function.
        # 2. Test other pivot selections, like the "Median-of-three" rule,
            # and apply different case-study circumstances.
        # 3. Should the program account for various array-types?
    
    
    ## Notes to self for Testing and Troubleshooting:
        # Take time to conceptually go through each block of code.
        # Track how the loops occur.
        # Track inputs & outputs.
        # Be sure the code & its action match conceptual approach.