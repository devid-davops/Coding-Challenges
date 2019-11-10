# Sum of Prime Factors

## Problem Statement
Display the sum of **unique prime factors** (if any exist) of a given integer, N.

>input: 500

>output: 2 + 5 = 7


## Approach
### Assumptions
1. The integer input has either _unique_ or _repeating_ prime factors, if any exist.
1. The operator for (floor) integer-division `//` rounds down.


### Solution Outline
1. Define a function that accepts a valid integer input, `N`.
1. **Divide and Conquer.**
    1. Set a new range of integers to consider as Prime Factors (**PF**).
    1. Conditionally perform checks on the new range.
        - Check for any factors of `N`.
        - Perform a "prime-check" to filter out non-prime numbers.
    1. Return the sum of prime factors found.



> _Updates will occur on Nov. 10, 2019_    ~ DBE


#### Divide and Conquer Section (with code excerpts)
* _Block A, Main:_
    * Check for invalid inputs:
        * IF valid: proceed (e.g., `N >= 2`).
        * IF invalid: print an `Invalid Entry` statement.
    * Set a new (inclusive) range of integers to consider as **PF**:
        * `[pf_min, pf_max]`
        * Where the smallest possible **PF** is a constant: `pf_min = 2`
        * Where the largest possible **PF** varies: `pf_max <= N//2`
    * Initialize an _auxiliary list_ to store Prime Factors found.
    * Perform checks to find base (unique) factors for each `current_integer` in the new _A-range_ `[2, pf_max]`:
        1. **Factor-Check**: Check if `N` is a multiple of `current_integer` via trial division:
            1. If `N % current_integer` equals zero: _Factor found, proceed to **prime-check**_
            2. Else: _Factor not found, check the next_ `current_integer`
        2. **Prime-Check**, filter out non-prime numbers.
        If factor found in A-range, Check if `current_integer` has PF:
            # For each possible_factor in B-range [2, `current_integer`):
                If `current_integer` % possible_factor == 0:
                    Break from current loop iteration.
            
            # Note: The else clause of a for-loop will run when no
            # "break" occurs, which means the current integer is 
            # both a factor and prime number (i.e., valid PF) of `N`.
            
            # Else:
                Append `current_integer` to list of **PF**.
    
    Conditionally return statement or results:
        If PF list is empty: return a string like "No PF found".
        Else: return a tuple of details: `(sum, [list], N)`

> _**Note:** An improvement would be to display, respectively, the frequency of occurrence of each base factor (e.g., 36 = 2^2 * 3^2)._









* _Block B, Print Details:_
    * 


---



> _Updates will occur on Nov. 10, 2019_    ~ DBE
***Block A*** and ***Block B*** can be implemented in _Python 3_ like this:

```python
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

```






## Extra Notes
### Example: Computing Unique Prime Factors

**Syntax Notes**
* When writing a Mathematical range: _brackets include, parens exclude_
    * `R: [inclusive, exclusive)`
* When using the range function in Python 3: _range(inclusive, exclusive)_
    * `range(2, 6)` returns a range of four integers from 2 up to, but not including, 6
    * `list(range(2, 6))` returns a list of the included integers: `[2, 3, 4, 5]`


**Given an integer `N`,**
Let `N = pf_i * pf_j`
* Where `pf_i` & `pf_j` are prime factors (**PF**) of `N`,
    1. Which may not be distinct,
    2. May have their own prime factors, but
    3. Only exist within the _inclusive range_: `[2, N//2]`

Consider the following two integers:
* `N = 22`
    * A list of **PF** of `N` would be: `[2, 11]`
    * Notice that each **PF** is unique and exists within the _range_ of:
        `2 <= x <= (N // 2)`
    * Here, each **PF** respectively equals an end-value of the _range_:
        * 2 equals the _lower-bound_
        * 11 equals the _upper-bound_.

* `N = 500`
    * A list of **PF** of N would be: `[2, 2, 5, 5, 5]`
    * Although not unique, each **PF** still exists within the range of:
        `2 <= x <= (N // 2)`
    * The list of unique **PF** would be: `[2, 5]`
        * A more accurately detailed output could show: `500 equals: 2^2 * 5^3`


---


### Improvements (optional but possibly fun)
1. Display, respectively, the frequency of occurrence of each base factor (e.g., 36 = 2^2 * 3^2).
2. Solve the original task with zero (or minimal) Trial Division.
3. Write the code such that it runs in sub-linear time.


### References:
1. [Python 3 Documentation](https://docs.python.org/3/index.html)
1. [Codecademy: Sum of Prime Factors Challenge](https://discuss.codecademy.com/t/challenge-sum-of-prime-factors/81035)
1. [Khan Academy: Prime factorization](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization)