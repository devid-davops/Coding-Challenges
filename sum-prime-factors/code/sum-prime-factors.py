def sum_prime_factors(N_given):
    """Accepts given integer N >= 2. Returns sum of prime factors and
    a list of all prime factors found as a tuple: (sum, [list]).
    
    Finds all prime factors for N using direct-search-factorization
    (trial division).
    """
    
    if N_given >= 2:
        pf_max = N_given//2
        pf = list()
        
        for current_integer in range(2, pf_max + 1):
            # Perform factor-check
            if N_given % current_integer == 0:
                # Perform prime-check, filter out non-prime numbers
                for possible_factor in range(2, current_integer):
                    if current_integer % possible_factor == 0:
                        break
                else:
                    pf.append(current_integer)
                # Note:
                # -> The else clause of a for-loop runs when no "break" occurs
                # -> Thus, here, current_integer is a prime factor of N.
                
        if not pf:
            return  ?  # ------------------------------------------------------------------------------------------------------------------------------ print("EMPTY") ... return None ?
        elif pf: 
            return (sum(pf), pf)




## define print_details()




N_arr = [-10, -6, 2, 3, 4, 6, 14, 15, 36, 50, 75, 154, 155, 500]

## Test each value manually
# N = N_arr[0]
# output = sum_prime_factors(N)
# print(f"""
# Number: {n}
# Sum of Prime Factors: {output[0]}
# Prime Factors: {output[-1]}
# """)


## Test via loop
for n in N_arr:
    try:
        output = sum_prime_factors(n)
        if # ------------------------------------------------------------------------------------------------------------------------------
            print(f"""
            Number: {n}
            Sum of Prime Factors: {output[0]}
            Prime Factors: {output[-1]}
            """)

        else:
            print(f"Sorry, no prime factors were found for {N_given}, try a different value.")
    
    except (TypeError, ValueError):
        print("Oops!  That was no valid number.  Try again.")












## DBE's Notes
""" Notes about Challenge:
    1. Display the sum of all prime factors (if any exist) of a given integer, N.
        -> input: 30
        -> output: 2 + 3 + 5 = 10

    References:
        [1] Python 3 Documentation 
            >> https://docs.python.org/3/index.html
        [2] Codecademy: Sum of Prime Factors Challenge
            >> https://discuss.codecademy.com/t/challenge-sum-of-prime-factors/81035
        [3] Khan Academy: Prime factorization
            >> https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization
"""


# David Booker-Earley's approach for this challenge:
    ## ** OVERVIEW **
        # 1. Define a function that accepts a valid input, N (integer).
        # 2. Set a new range of integers to consider as Prime Factors.
        # 3. Perform checks.
            # 3.a. Check for any factors of N.
            # 3.b. Conditionaly perform a "prime-check" to filter out non-prime numbers.
        # 4. Return the sum of the found prime factors.
    
    
    ## ** ASSUMPTIONS **
        # 1. The integer input may have distinct or repeating prime factors (if any exist).
        # 2. The operator for (floor) integer-division "//" rounds down.
    
    
    ## ** SOLUTION **
      # Define a function that accepts a given integer N.
        # Check for invalid inputs:
            # IF valid: proceed (e.g., check if type is integer and N > = 2).
            # IF invalid: print "Invalid entry." or do nothing.
        
        # Solution 1 - Brute Force
        # Use direct search factorization (trial division).
            # Set new range of integers to consider as PFs: [pf_min, pf_max]
                # pf_min = 2
                # .. (constant) the smallest possible prime factor
                
                # pf_max <= N//2
                # .. (variable) the largest possible prime factor
            
            # Initialize auxiliary list to store Prime Factors
                # pf = list()
            
            # For each current_integer in new A-range [2, pf_max]:
                # .. perform factor-check
                # Check if N is a multiple of current_int via trial division:
                    # If N % current_int == 0: factor found, proceed to prime-check
                    # Else: go to next current_int
                
                # .. perform prime-check, filter out non-prime numbers
                # If factor found in A-range, Check if current_integer has factors:
                    # For each possible_factor in B-range [2, current_integer):
                        # If current_integer % possible_factor == 0:
                            # Break from current loop iteration
                    
                    # .. The else clause of a for-loop will run when no "break" occurs,
                    # .. which means current_integer is both a prime number and a factor of N.
                    # Else:
                        # Append current_integer to list of PFs
            
            # return tuple: (sum of list, [list of prime factors])




        
        
        
        
        # Solution 2 - ?
        # Minimal Direct Search Factorization.
            # ?
            
            
            
            
            # Divide and Conquer -> ? :
                # Setup sub-function(s):
                    # Block A -> Main and ?:
                        # ?
                    
                    # Block B -> ?:
                        # ?
      
      
      
      
      
      # Call main function on a given input.
      # Print results.
    
    
    ## ** EXAMPLE **
        # Given an integer N, 
        # Let N = pf_i * pf_j  
            # where pf_i & pf_j are prime factors (PFs) of N,
            # which may not be distinct,
            # may have their own prime factors, but
            # only exist within the inclusive range: [2, N//2]
        # ---------------------------------------------------------------------------------------------- include updated example
      
      
      
    ## ** IMPROVEMENTS (Extra Practice for Fun) **
        # 1. Solve the original task with zero (or minimal) Trial Division.
        # 2. Find the sum of each "unique" prime factor of the given number N.
        # 3. Write the code such that it runs in sub-linear time.
    
    
    ## Notes to self for Testing and Troubleshooting:
        # Take time to conceptually go through each block of code.
        # Track how the loops occur.
        # Track inputs & outputs.
        # Be sure the code & its action match conceptual approach.




## Temporary Conceptual Analysis
""" 
Extra Info to include, Example: ---------------------------------------------------------------------------------------------- update & include brief example
    N = 22 = 2 * 11
    .. new range: [2 3 4 5 ... 10 11]
    .. [inclusive, exclusive)






_________________________________________ Exclude info below

Test these values for N:
    -10 --> error should occur
    -6 --> error should occur
    2
    3
    4
    6
    14
    15
    36
    50
    75
    154
    155
    500


_________________________________________

Testing main concept in Python -->> it works:
    >>> pf = list()
    >>> pf
    []
    >>>
    >>> 
    >>> N = 22
    >>> 
    >>> for CI in range(2, N//2 + 1):
    ...     if N % CI == 0:
    ...         # Prime Check Starts Here
    ...         for PosFac in range(2, CI):
    ...             if CI % PosFac == 0:
    ...                 break
    ...         else:
    ...             pf.append(CI)
    ... 
    >>> 
    >>> 
    >>> pf
    [2, 11]
    >>>
    >>> 
    >>> sum(pf)
    13
    >>>


_________________________________________

Testing concept of TRUE-FALSE with empty sequences in Python -->> it works:
    >>> pf = list()
    >>> sum(pf)
    0   
    >>> pf
    []  
    >>> if not pf:         
    ...     print("EMPTY") 
    ... elif pf: 
    ...     print("FULL")
    ... 
    EMPTY
    >>> pf.append(2)
    >>> pf
    [2]
    >>>    
    >>> 
    >>> if not pf:
    ...     print("EMPTY")
    ... elif pf:
    ...     print("FULL")
    ... 
    FULL
    >>>


__________________________________________________________________________

.. Trial Division approach should be fine for relatively small numbers, N <= 50.

50 // 2
25
5 * 5

__________________________________________________________________________


500 can be split like this:
    5 100
    5 10 10
    5 5 2 5 2
    5^3 * 2^2
500 // 2
250
.. Loop A: range from 2 to 250
.. Loop B: range from 2 to the current_integer in Loop A
.. code would iterate ineffectively looping A & B.





Example A: 15
    PFs of 15 are 3 and 5.
    
    Use "//" to get the max value (upper-bound) for the range of pfs for 15:
        15 // 2 = 7
        Range of PFs: [2, 7]




Example B: 75
    Ask "Can I divide 75 by 2, how about 3, or 5, etc.?
    75 can be split with integers (no "//") like this:
        .. 75
        .. 3 * 25
        .. 3 * 5 * 5    




Example C: 154
        .. 2 * 77
        .. 2 * 7 * 11

Visualize with integer-division:
.. Note that using "N // 2" will provide only the range of PFs,
.. Using the "//" operator carelessly may result in betrayal for odd numbers.
154 // 2 (also for "155 // 2")
        ,,
    2       77
            ,,
        7      11



"""