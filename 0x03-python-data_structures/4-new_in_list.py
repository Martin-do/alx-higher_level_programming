#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ls_copy = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return ls_copy
    else:
        ls_copy[idx] = element
        return ls_copy


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
