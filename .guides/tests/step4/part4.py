#!/usr/local/bin/python3
"""
Assess part 2, the function stub for get_dst

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_step2(file,func):
    """
    Checks that the stub for the given function is correct
    
    Parameter file: The file to check
    Precondition: file is a string
    
    Parameter func: The function to check
    Precondition: func is a string, a name of a function in file
    """
    result = verifier.grade_func_stub(file,func,0)
    if not result[0]:
        print("The function stub for %s looks correct." % repr(func))
    return result[0]


if __name__ == '__main__':
    sys.exit(check_step2('currency.py','get_dst'))