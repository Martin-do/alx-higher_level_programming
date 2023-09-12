#!/usr/bin/python3
import sys


def print_stats_code(sc_dict, sc_list):
    for codes in sc_list:
        print("{:d}: {:d}".format(codes, sc_dict[codes]))
        sc_dict[codes] = 0


def compute_metrics():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    counter  = 0
    ls_of_sc = []
    
    for line in sys.stdin:
        data = line.split(" ")
        sc = int(data[7])
        fl_sz = int(data[8])
        
        total_size += fl_sz
        if sc in status_codes:
            ls_of_sc.append(sc)
            status_codes[sc] += 1
        counter += 1
        if counter == 10:
            print(ls_of_sc)
            print_stats_code(status_codes, ls_of_sc)
            ls_of_sc.clear()
            counter = 0

compute_metrics()
