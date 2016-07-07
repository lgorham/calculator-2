"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def evaluate_function():
    """will take the user's prefix calculation and return the answer"""
    user_input = None
    
    while user_input != 'q':
        user_input = raw_input("Input your prefixed calculation: ")
        tokenized_string = user_input.split(" ")

        if len(tokenized_string) == 3:
            int1 = int(tokenized_string[1])
            int2 = int(tokenized_string[2])
        elif len(tokenized_string) == 2:
            int1 = int(tokenized_string[1])

        if tokenized_string[0] == '+':
            print add(int1, int2)
        elif tokenized_string[0] == '-':
            print subtract(int1, int2)
        elif tokenized_string[0] == '*':
            print multiply(int1, int2)
        elif tokenized_string[0] == '/':
            print divide(int1, int2)
        elif tokenized_string[0] == 'square':
            print square(int1)
        elif tokenized_string[0] == 'cube':
            print cube(int1)
        elif tokenized_string[0] == 'pow':
            print power(int1, int2)
        elif tokenized_string[0] == 'mod':
            print mod(int1, int2)




evaluate_function()