## DBE's alternative solution for the modified fizz-buzz challenge.

# Print Conditionally (check constraints).
# Print "Fizz" for multiples of three (m3), "Buzz" for m5, "Water" for m7.
for number in range(1, 201):
    
    # Out of the 7 conditions, 4 include m3 --> m3, m375, m35, m37.
    if number%3 == 0:
        print('Fizz', end='') # prints the next item behind "Fizz".
        # Append based on 3 conditions --> m375, m35, m37
        if number%5 == 0 and number%7 == 0:
            print("WaterBuzz")
        elif number%5 == 0 and number%7 != 0:
            print('Buzz')
        elif number%7 == 0 and number%5 !=0:
            print('Water')
        else:
            print('') # newline is needed due to "print(x, end='')"
    
    # Print based on 2 conditions --> m7, m75.
    elif number%7 == 0:
        print('Water', end='')
        # Append based on 1 condition --> m75
        if number%5 == 0 and number%3 != 0:
            print('Buzz')
        else:
            print('')
    
    # Print based on 1 condition --> m5.
    elif number%5 == 0:
        print('Buzz')
    
    else:
        print(number)




## DBE's Notes
""" Notes about Modified Challenge:
    1. Print numbers from 1 to 200, but print the word X rather than a 
       number based on multiples of N:
            * Print "Fizz" for multiples of three.
            * Print "Buzz" for multiples of five.
            * For numbers which are multiples of seven, print "Water".
            * For multiples of both three and five, print "FizzBuzz".
            * For multiples of both three and seven, print "FizzWater".
            * For multiples of both five and seven, print "WaterBuzz".
            * For multiples of three, five, and seven, print "FizzWaterBuzz".
            -> output example:  1, 2, Fizz, 4, Buzz, 6, Water, ...
    2. Write the shortest code possible.
    
    References:
        [1] HackerRank 
            >> https://www.hackerrank.com/challenges/fizzbuzz/problem
        [2] Python 3 Documentation 
            >> https://docs.python.org/3/index.html
"""


# David Booker-Earley's approach-2 for this challenge:
    ## ** ASSUMPTIONS **
        # 1. The given range and corresponding outputs are integers.
    
    
    ## ** SOLUTION 2 - Use Modulus, %, and Print **
        # Implement updates to Solution 1:
            # Use the Modulus, or Modulo, operator, "%".
            # Don't create auxiliary lists (don't store data, just print).
    
    
    ## Notes to self for Testing and Troubleshooting:
        # Take time to conceptually go through each block of code.
        # Track how the loops occur.
        # Track inputs & outputs.
        # Be sure the code & its action match conceptual approach.