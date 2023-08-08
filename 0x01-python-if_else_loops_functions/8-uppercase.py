#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            output = chr(ord(i) - 32)
        else:
            output = i
        print("{}".format(output), end="")
    print("")
