#!/usr/bin/python3



if __name__ == "__main__":
    from sys import argv
    
    arg_count = len(argv) - 1
    if arg_count == 0:
        response = "arguments."
    elif arg_count == 1:
        response = "argument:"
    else:
        response = "arguments:"
    print("{} {}".format(arg_count, response))
    if arg_count != 0:
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
