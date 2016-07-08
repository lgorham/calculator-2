def add(arg_list):
    """ Add any number of integers together """

    total = 0

    for i in arg_list:
        total += i 
    return total

def subtract(arg_list):
    """Subtract any number of numbers from num1"""

    total = arg_list[0]

    for i in arg_list[1:]:
        total -= i
    return total
   

def multiply(arg_list):
    """ Multiply any number of integers together """

    total = 1

    for i in arg_list:
        total = total * i
    return total

def divide(arg_list):
    """ Divide num1 by any number of successive arguments """
    
    total = arg_list[0]

    for i in arg_list[1:]:
        total = total / i
    return total

def square(arg_list):
    """squaring num1"""

    return arg_list[0]**2

def cube(arg_list):
    """cubing num1"""

    return arg_list[0]**3

def power(arg_list):
    """ return the value of num1 to the power of any number of successive arguments """
    
    total = arg_list[0]

    for i in arg_list[1:]:
        total = total**i
    return total

def mod(arg_list):
    """ return the remainder of num1 divided by any number of successive arguments """
    
    remainder = int(arg_list[0])

    for i in arg_list[1:]:
        remainder = remainder % int(i)
    return remainder