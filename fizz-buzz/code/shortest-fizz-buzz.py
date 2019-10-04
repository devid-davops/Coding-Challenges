# Store a list of numbers in the given range (1 to 200).
n = 200
numbers = list(range(1, n + 1))

# Conditions to be met (Constraints).
m3 = list(range(3, 1 + numbers[-1], 3))
m5 = list(range(5, 1 + numbers[-1], 5))
m7 = list(range(7, 1 + numbers[-1], 7))

# Dictionary of condition-based words needed for printing.
Words = {
    'M3': 'Fizz',
    'M5': 'Buzz',
    'M7': 'Water',
    'M35': 'FizzBuzz',
    'M37': 'FizzWater',
    'M75': 'WaterBuzz',
    'M375': 'FizzWaterBuzz'
}

# Print Conditionally (check constraints).
# Print "Fizz" for multiples of three (m3), "Buzz" for m5, "Water" for m7.
for number in numbers:
    # Check for multiples of all three
    if number in m3 and number in m5 and number in m7:
        print(Words['M375']) # prints 'FizzWaterBuzz'
    
    # Check for multiples of pairs
    elif number in m3 and number in m5:
        print(Words['M35'])
    elif number in m3 and number in m7:
        print(Words['M37'])
    elif number in m5 and number in m7:
        print(Words['M75'])
    
    # Check for individuals
    elif number in m3:
        print(Words['M3'])
    elif number in m5:
        print(Words['M5'])
    elif number in m7:
        print(Words['M7'])
    
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


# David Booker-Earley's approach for this challenge:
    ## ** ASSUMPTIONS **
        # 1. The given range and corresponding outputs are integers.
    
    
    ## ** SOLUTION 1 - Data Structures **
        # Store a list of numbers in the given range (1 to n).
        
        # Consider every multiple as a "constraint".
            # Each constraint (key) will print a unique word (value).
        
        # Store a list of numbers for each constraint as a reference.
            # If "range(start,stop)" is used, add 1 in "stop" to ensure
            # the last value, n, is accounted for.
        
        # Store word-constraints in a dictionary (preserves core concept).
            # This preserves the code's concept and functionality while
            # ... allowing changes to the constraints needed for printing.
            # Define it before the main loop to provide clean code
            # ... and easier troubleshooting.
            # Use a leading-uppercase to distinguish dict from lists.
        
        # Print results conditionally (check constraints).
        # "Fizz" for multiples of three (m3), "Buzz" -> m5, "Water" -> m7.
            # Iterate through lists and Check if number is in constraints:
                # If yes, print the corresponding word.
                # If no, print the number.
    
    
    ## ** IMPROVEMENTS (Extra Practice: Optional but Fun) **
        # 1. Solve this challenge without auxiliary variables / lists.
        # 2. Can this code be reduced or more concise?
        # 3. Can constraints be checked using "if x is not y"?
    
    
    ## Notes to self for Testing and Troubleshooting:
        # Take time to conceptually go through each block of code.
        # Track how the loops occur.
        # Track inputs & outputs.
        # Be sure the code & its action match conceptual approach.