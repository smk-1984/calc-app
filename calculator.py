def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def percentage(part, whole):
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100

def power(base, exponent):
    return base ** exponent


def modulo(a, b):
    # Guard against modulo-by-zero, since it's mathematically undefined
    # (mirrors the same check used in divide()).
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b