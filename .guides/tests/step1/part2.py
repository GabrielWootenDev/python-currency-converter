#!/usr/local/bin/python3
"""
Assess part 2, creating the app file

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 31, 2018
"""
import verifier
import sys


def check_step2(file):
    """
    Checks that the script docstring and import is correct.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_docstring(file,0)
    if not result[0]:
        result = verifier.grade_app_structure(file,0)
    if not result[0]:
        print("The outline of file %s looks correct." % repr(file))
    return result[0]


if __name__ == '__main__':
    sys.exit(check_step2('exchangeit.py'))