#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:36:32 2022

@author: mehradhq
"""

#problem 1: you don't print the calculator logo for each operation.
print ("""
       _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

    """)

#problem 2: here she defined a dictionary for the operations and functions for add...
def calculator(parameter_one,parameter_two,operation_type):
    if operation_type=="+":
        result=parameter_one+parameter_two
    elif operation_type=="-":
        result=parameter_one-parameter_two
    elif operation_type=="*":
        result=parameter_one*parameter_two
    elif operation_type=="/":
        result=parameter_one/parameter_two
    else:
        return ("the operation was not defined! ")
    return (result)



def asking():
    first=float(input("what's the first number?: "))
    operation=input("+\n-\n*\n/\npick an operation: ")
    second=float(input("what's the next number?: "))
    answer=calculator(first, second, operation)
    end=False
    if answer=="the operation was not defined! ":
        return "the operation was not defined! "
    print (answer)
    while not end:
        further=input(f"type 'y' to continue working with {answer} and 'n' to start a new calculator, press 'c' to cancel: ")
        if further=='y':
            first=answer
            print (f"\nfirst={first}")
            operation=input("+\n-\n*\n/\npick an operation: ")
            second=float(input("what's the next number?: "))    
            print (calculator(first, second, operation))
        elif further=='n':
            asking()
        elif further=='c':
            end=True
            return "finish"
print (asking())
print ("the program is finished.")