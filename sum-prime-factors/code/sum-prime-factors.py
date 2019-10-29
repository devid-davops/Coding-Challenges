## code block


## code block




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
        # 1. Accept a valid input.
        # 2. 
        # 3. 
        # 4. 
    
    
    ## ** ASSUMPTIONS **
        # 1. The integer input may have distinct or repeating prime factors (if any exist).
        # 2. The operator for (floor) integer-division "//" rounds down.
    
    
    ## ** SOLUTION **
      # Given an integer N, let N = pf_i * pf_j 
        # .. where pf_i & pf_j are prime factors of N,
        # .. which may not be distinct,
        # .. may have their own prime factors, but
        # .. only exist within the inclusive range: [2, N//2]
      
      
      
      # Define a function that accepts a given integer N.
        # Check for invalid inputs:
            # IF valid: proceed (e.g., check if type is integer and N > = 2).
            # IF invalid: print "Invalid entry." or do nothing.
        
        
        
        
        
        # Solution 1 - With Direct Search Factorization (trial division).
            # 
        
        
        
        
        
        # Solution 2 - Without Direct Search Factorization.
            # 
        
        
        
        
        
        # Divide and Conquer -> ? :
            # Setup sub-function(s):
                # Block A -> Main and ?:
                    # ?
                
                # Block B -> ?:
                    # ?
      
      
      
      
      
      # Call main function on a given input.
      # Print results.
    
    
    ## ** IMPROVEMENTS (Extra Practice for Fun) **
        # 1. 
        # 2. 
        # 3. 
    
    
    ## Notes to self for Testing and Troubleshooting:
        # Take time to conceptually go through each block of code.
        # Track how the loops occur.
        # Track inputs & outputs.
        # Be sure the code & its action match conceptual approach.




## Temporary Conceptual Analysis
""" Note: A Prime Factor is a factor that is a prime number.

Known: N = pf_i * pf_j 
    .. where pf_i & pf_j are prime factors of a given number N,
    .. which may not be distinct,
    .. may have their own prime factors, but
    .. exist within the inclusive range: [2, N//2]


Approach for finding all PFs:
    Range of integers to consider: [pf_min, pf_max]
        .. Assume the (floor) integer-division "//" operator rounds down.
        .. The smallest possible prime factor: pf_min = 2
        .. The largest possible prime factor: pf_max <= N//2
    Check if N is a multiple of integers in the new range [pf_min, pf_max]:
        Trial-Division: divide N by values in new range 




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