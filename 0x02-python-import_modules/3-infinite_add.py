#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_count = len(argv) - 1
    sum = 0
    if arg_count != 0:
        for i in range(1, len(argv)):
            sum += int(argv[i])
    print("{}".format(sum))
