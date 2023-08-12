#!/usr/bin/python3


def multiple_returns(sentence):
    str_len = len(sentence)
    if sentence is not None and str_len != 0:
        first_char = ""
        for i in sentence:
            first_char += i
            break
        return (str_len, first_char)
    else:
        return (str_len, None)


if __name__ == '__main__':
    sentence = ""
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
