"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    operation = raw_input('>')
    if operation == 'q':
        break
    operation_list = operation.split()

    if operation_list[0] == '+':
        answer = add(int(operation_list[1]), int(operation_list[2]))
    elif operation_list[0] == '-':
        answer = subtract(int(operation_list[1]), int(operation_list[2]))
    elif operation_list[0] == '*':
        answer = multiply(int(operation_list[1]), int(operation_list[2]))
    elif operation_list[0] == '/':
        answer = divide(int(operation_list[1]), int(operation_list[2]))
    elif operation_list[0] == 'square':
        answer = square(int(operation_list[1]))
    elif operation_list[0] == 'cube':
        answer = cube(int(operation_list[1]))
    elif operation_list[0] == 'pow':
        answer = power(int(operation_list[1]), int(operation_list[2]))
    elif operation_list[0] == 'mod':
        answer = mod(int(operation_list[1]), int(operation_list[2]))
    else:
        answer = "Invalid input!"
    print answer

print "Good Bye"
