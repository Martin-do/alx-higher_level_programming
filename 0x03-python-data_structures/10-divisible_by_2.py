#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    new_ls = []
    for i in my_list:
        if i % 2 == 0:
            new_ls.append(True)
        else:
            new_ls.append(False)
    return new_ls


if __name__ == '__main__':
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    st = "{:d} {:s} divisible by 2"
    while i < len(list_result):
        print(st.format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1
