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
        integer_section = tokenized_string[1:]

        integer_list = []
        for i in integer_section:
            int_form = int(i)
            # converting to int first because append(int(i)) was returning a string
            integer_list.append(int_form)

        if tokenized_string[0] == '+':
            print add(integer_list)
        elif tokenized_string[0] == '-':
            print subtract(integer_list)
        elif tokenized_string[0] == '*':
            print multiply(integer_list)
        elif tokenized_string[0] == '/':
            print divide(integer_list)
        elif tokenized_string[0] == 'square':
            print square(integer_list)
        elif tokenized_string[0] == 'cube':
            print cube(integer_list)
        elif tokenized_string[0] == 'pow':
            print power(integer_list)
        elif tokenized_string[0] == 'mod':
            print mod(integer_list)




evaluate_function()