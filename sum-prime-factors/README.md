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
1. Define a function that accepts a valid integer input, N.
1. **Divide and Conquer.**
    1. Set a new range of integers to consider as Prime Factors (PFs).
    1. Conditionally perform checks.
        - Check for any factors of N.
        - Perform a "prime-check" to filter out non-prime numbers.
    1. Return the sum of the found prime factors.



> _Updates will occur on Nov. 10, 2019_    ~ DBE
#### Divide and Conquer Section (with code excerpts)
* _Block A, Main:_
    * 

* _Block B, Print Details:_
    * 


---



> _Updates will occur on Nov. 10, 2019_    ~ DBE
***Block A*** and ***Block B*** can be implemented in _Python 3_ like this:

```python
def 



def


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