from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Return the sum of *a* and *b*.

    >>> add(1, 2)
    3
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Return the difference of *a* and *b*.

    >>> subtract(5, 3)
    2
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Return the product of *a* and *b*.

    >>> multiply(4, 3)
    12
    """
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Return the quotient of *a* divided by *b*.

    Raises
    ------
    ValueError
        If *b* is zero.

    >>> divide(10, 2)
    5.0
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
