def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # NOTE: this "simplification" is the deliberate regression for CALC-10 —
    # it removes the zero-check that test_divide_by_zero relies on.
    return a / b


def percentage(part, whole):
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100

def power(base, exponent):
    return base ** exponent