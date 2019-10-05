# FizzBuzz

## Problem Statement
Modified from [HackerRank](https://www.hackerrank.com/challenges/fizzbuzz/problem)


### Notes about the modified fizz-buzz challenge:
1. Print numbers from 1 to 200, but print the word X rather than a 
number based on multiples of N:
  * Print "Fizz" for multiples of three.
  * Print "Buzz" for multiples of five.
  * For numbers which are multiples of seven, print "Water".
  * For multiples of both three and five, print "FizzBuzz".
  * For multiples of both three and seven, print "FizzWater".
  * For multiples of both five and seven, print "WaterBuzz".
  * For multiples of three, five, and seven, print "FizzWaterBuzz".
    - output example:  1, 2, Fizz, 4, Buzz, 6, Water, ...

2. Write the shortest code possible.


## Approach
### Assumptions
1. The given range and corresponding outputs are integers.


### Solution 1 - Data Structures
1. Store a list of numbers in the given range (1 to n).
1. Consider every multiple as a "constraint".
    1. Each constraint (key) will print a unique word (value).
1. Store a list of numbers for each constraint as a reference.
    1. If "range(start,stop)" is used, add 1 in "stop" to ensure
    1. the last value, n, is accounted for.
1. Store word-constraints in a dictionary (preserves core concept).
    1. This preserves the code's concept and functionality while allowing changes to the constraints needed for printing.
    1. Define it before the main loop to provide clean code and easier troubleshooting.
    1. Use a leading-uppercase to distinguish dict from lists.
1. Print results conditionally (check constraints).
    1. Iterate through lists and check if number is in constraints:
        1. If yes, print the corresponding word.
        1. If no, print the number.


### Solution 2 - Use Modulus, %, and Print
1.  Implement updates to Solution 1:
    1. Use the Modulus, or Modulo, operator, "%".
    1. Don't create auxiliary lists (don't store data, just print).


## Extra Notes
### Improvements (optional but possibly fun)
1. Solve this challenge without auxiliary variables / lists.
2. Can this code be reduced or more concise?
3. Can constraints be checked using "if x is not y"?


### References:
1. [HackerRank](https://www.hackerrank.com/challenges/fizzbuzz/problem)
2. [Python 3 Documentation](https://docs.python.org/3/index.html)