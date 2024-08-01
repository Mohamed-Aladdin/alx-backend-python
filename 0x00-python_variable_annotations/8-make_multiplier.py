#!/usr/bin/env python3
"""Task 8 Module"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Write a type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a function that
    multiplies a float by multiplier
    """

    return lambda x: x * multiplier
