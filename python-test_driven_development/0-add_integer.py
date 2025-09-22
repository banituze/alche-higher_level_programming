#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """Adds two numbers
    Args:
        a - first number input
        b - second number input
    """
    if type(a) not in [int] and type(a) not in [float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int] and type(b) not in [float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
