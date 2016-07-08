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
        num_section = tokenized_string[1:]

        num_list = []
        try:
            for i in num_section:
                num_form = float(i)
                # converting to int first because append(int(i)) was returning a string
                num_list.append(num_form)
        except:
            print "You did not properly enter your calculation: operator followed by operands"
            continue

        try:
            test_for_args = num_list[0]
        except:
            print "You did not input any arguments"
            continue


        if tokenized_string[0] == '+':
            print add(num_list)
        elif tokenized_string[0] == '-':
            print subtract(num_list)
        elif tokenized_string[0] == '*':
            print multiply(num_list)
        elif tokenized_string[0] == '/':
            print divide(num_list)
        elif tokenized_string[0] == 'square':
            print square(num_list)
        elif tokenized_string[0] == 'cube':
            print cube(num_list)
        elif tokenized_string[0] == 'pow':
            print power(num_list)
        elif tokenized_string[0] == 'mod':
            print mod(num_list)
        else:
            print "You did not input a proper operator"




evaluate_function()