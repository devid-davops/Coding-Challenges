def sum_unique_prime_factors(N_given):
    """Accepts given integer N >= 2. Returns a tuple of the sum of only
    unique prime factors, a list of unique prime factors found, and N.
    
    Output: (sum, [list], N).
    
    Finds all prime factors for N using direct-search-factorization,
    i.e., trial division.
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
                # The else clause of a for-loop runs when no "break" occurs.
                # Thus, here, current_integer is a prime factor of N.
        
        if not pf:
            return f"No Prime Factor was found for {N_given}, try again."
        
        elif pf: 
            return (sum(pf), pf, N_given)
    
    else:
        return f"Oops! {N_given} is not a valid number. Try again."


def print_details(details):
    """Prints organized results of sum_unique_prime_factors()."""
    
    if isinstance(details, tuple):
        print(f"""Great choice! Here are the details:
        Number Given: {details[-1]}
        Sum of Unique Prime Factors: {details[0]}
        Unique Prime Factor(s): {details[1]}
        """)
    
    else:
        print(details)


## Test each value manually
N_list = [-10, -6, 2, 3, 4, 6, 14, 15, 30, 36, 50, 75, 154, 155, 412, 500]
N = N_list[-2]
print_details( sum_unique_prime_factors(N) )










# ## Test via loop
# for n in N_list:
#     try:
#         
#     except (TypeError, ValueError):
#         print("Oops!  That was no valid number.  Try again.")










## DBE's Notes
""" Notes about Challenge:
    1. Display the sum of unique prime factors (if any exist) of a given integer, N.
        -> input: 500
        -> output: 2 + 5 = 7

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
        # 1. Define a function that accepts a valid integer input, N.
        # 2. Set a new range of integers to consider as Prime Factors (PF).
        # 3. Conditionally perform checks.
            # 3.a. Check for any factors (unique or not) of N.
            # 3.b. Perform a "prime-check" to filter out non-prime numbers.
        # 4. Return the sum of the found (unique or not) prime factors.
    
    
    ## ** ASSUMPTIONS **
        # 1. Integer input has unique or repeating prime factors if any exist.
        # 2. Operator for (floor) integer-division "//" rounds down.
    
    
    ## ** SOLUTION **
      # Define a function that accepts a given integer N.
        # Check for invalid inputs:
            # IF valid: proceed (e.g., check if type is integer and N > = 2).
            # IF invalid: print "Invalid entry." or do nothing.
        
        # Solution 1 - Brute Force
        # Use direct search factorization (trial division).
            # Set new range of integers to consider as PF: [pf_min, pf_max]
                # pf_min = 2
                # -> (constant) the smallest possible prime factor
                
                # pf_max <= N//2
                # -> (variable) the largest possible prime factor
            
            # Initialize auxiliary list to store Prime Factors.
                # pf = list()
            
            # For each current_integer in new A-range [2, pf_max],
            # Perform checks to find base (unique) factors:
                ## Note: An improvement would be to display, respectively,
                ## the frequency of occurrence of each base factor
                ## (e.g., 36 = 2^2 * 3^2).
                
                # Perform factor-check.
                # Check if N is a multiple of current_int via trial division:
                    # If N % current_int == 0: 
                        # Factor found, proceed to prime-check.
                    # Else: go to next current_int.
                
                # Perform prime-check, filter out non-prime numbers.
                # If factor found in A-range, Check if current_int has PF:
                    ## For each possible_factor in B-range [2, current_int):
                        # If current_int % possible_factor == 0:
                            # Break from current loop iteration.
                    
                    ## Note: The else clause of a for-loop will run when no
                    ## "break" occurs, which means the current integer is 
                    ## both a factor and prime number (i.e., valid PF) of N.
                    
                    ## Else:
                        # Append current_int to list of PF.
            
            # Conditionally return statement or results:
                # If PF list is empty: return a string like "No PF found".
                # Else: return a tuple of details: (sum, [list], N)
      
      # Call main function on a given input.
      # Print results.
    
    
    ## ** CONCEPTUAL EXAMPLE **
        # Given an integer N, Let N = pf_i * pf_j  
            # where pf_i & pf_j are prime factors (PF) of N,
            # which may not be distinct,
            # may have their own prime factors, but
            # only exist within the inclusive range: [2, N//2]
            ## Syntax Note on a Mathematical range:
                ## brackets include, parens exclude
                ## Range: [inclusive, exclusive)
        
        # Consider the following two integers:
        # N = 22
            # A list of PF of N would be: [2, 11]
            # Notice that each PF is unique and exists within the range of:
            # 2  <=  x  <=  (N // 2)
                # Here, each PF respectively equals an end-value of the range,
                # 2 is the lower-bound and 11 is the upper-bound.
        # N = 500
            # A list of PF of N would be: [2, 2, 5, 5, 5]
            # Although not unique, each PF still exists within the range of:
            # 2  <=  x  <=  (N // 2)
            # The list of unique PF would be: [2, 5]
            # A more accurately detailed output could show: "500 = 2^2 * 5^3"
    
    
    ## ** IMPROVEMENTS (Extra Practice for Fun) **
        # 1. Display, respectively, the frequency of occurrence of each base factor (e.g., 36 = 2^2 * 3^2).
        # 2. Solve the original task with zero (or minimal) Trial Division.
        # 3. Write the code such that it runs in sub-linear time.
    
    
    ## Notes to self for Testing and Troubleshooting:
        # Take time to conceptually go through each block of code.
        # Track how the loops occur.
        # Track inputs & outputs.
        # Be sure the code & its action match conceptual approach.
