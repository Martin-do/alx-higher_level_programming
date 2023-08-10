#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv, exit 
    from calculator_1 import add, sub, mul, div

    arg_count = len(argv) - 1

    if arg_count != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    if arg_count == 3:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] in ["+", "-", "*", "/"]:
            if argv[2] == "+":
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif argv[2] == "-":
                print("{} + {} = {}".format(a, b, sub(a, b)))
            elif argv[2] == "*":
                print("{} + {} = {}".format(a, b, mul(a, b)))
            elif argv[2] == "/":
                print("{} + {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
