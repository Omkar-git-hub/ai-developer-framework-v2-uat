"""Basic calculator module for AI Developer Framework UAT."""


def add(a, b):
    """Return the sum of two values."""
    return a + b


def subtract(a, b):
    """Return the difference between two values."""
    return a - b


def multiply(a, b):
    """Return the product of two values."""
    return a * b


def divide(a, b):
    """Return the division result."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b
