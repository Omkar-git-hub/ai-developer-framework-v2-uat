from numbers import Number
from typing import Union

__all__ = ["add", "subtract", "multiply", "divide"]


def add(a: Number, b: Number) -> Number:
    """
    Return the sum of ``a`` and ``b``.

    Parameters
    ----------
    a : int or float
        First addend.
    b : int or float
        Second addend.

    Returns
    -------
    int or float
        The arithmetic sum.
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Return the difference of ``a`` and ``b``.

    Parameters
    ----------
    a : int or float
        Minuend.
    b : int or float
        Subtrahend.

    Returns
    -------
    int or float
        The arithmetic difference.
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Return the product of ``a`` and ``b``.

    Parameters
    ----------
    a : int or float
        Multiplicand.
    b : int or float
        Multiplier.

    Returns
    -------
    int or float
        The arithmetic product.
    """
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Return the quotient of ``a`` divided by ``b``.

    Parameters
    ----------
    a : int or float
        Numerator.
    b : int or float
        Denominator.

    Returns
    -------
    int or float
        The arithmetic quotient.

    Raises
    ------
    ValueError
        If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b