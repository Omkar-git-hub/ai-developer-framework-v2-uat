"""
Calculator module providing basic arithmetic operations.
"""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Return the sum of *a* and *b*.

    Parameters
    ----------
    a, b : int or float
        Operands to be added.

    Returns
    -------
    int or float
        The arithmetic sum.
    """
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """
    Return the difference of *a* and *b*.

    Parameters
    ----------
    a, b : int or float
        Operands where *a* is the minuend and *b* the subtrahend.

    Returns
    -------
    int or float
        The arithmetic difference.
    """
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """
    Return the product of *a* and *b*.

    Parameters
    ----------
    a, b : int or float
        Operands to be multiplied.

    Returns
    -------
    int or float
        The arithmetic product.
    """
    return a * b

def divide(a: Number, b: Number) -> Number:
    """
    Return the quotient of *a* divided by *b*.

    Parameters
    ----------
    a, b : int or float
        Operands where *a* is the dividend and *b* the divisor.

    Returns
    -------
    int or float
        The arithmetic quotient.

    Raises
    ------
    ValueError
        If *b* is zero.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b