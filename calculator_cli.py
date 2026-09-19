import argparse
import sys

from calculator import add, subtract, multiply, divide, percentage, power, modulo

# Maps the CLI's operation name straight onto the matching calculator.py
# function, so adding a new function here is a one-line change.
OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "percentage": percentage,
    "power": power,
    "modulo": modulo,
}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simple calculator CLI")
    parser.add_argument("operation", choices=OPERATIONS.keys())
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args(argv)

    func = OPERATIONS[args.operation]
    try:
        result = func(args.a, args.b)
    except ValueError as exc:
        # Domain errors (e.g. divide/modulo by zero) get a clean message on
        # stderr and a non-zero exit code, instead of a raw traceback.
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
