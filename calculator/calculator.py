"""Petites fonctions mathématiques + une mini CLI."""

import math


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


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take sqrt of a negative number")
    return math.sqrt(a)


OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "modulo": modulo,
    "sqrt": sqrt,
}


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=OPERATIONS.keys())
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float, nargs="?", default=None)
    args = parser.parse_args(argv)

    func = OPERATIONS[args.operation]
    if args.operation == "sqrt":
        result = func(args.a)
    else:
        if args.b is None:
            parser.error(f"operation '{args.operation}' needs two numbers")
        result = func(args.a, args.b)

    print(result)
    return result


if __name__ == "__main__":
    main()
