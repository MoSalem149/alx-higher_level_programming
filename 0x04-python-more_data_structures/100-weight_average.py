#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num_tuple = 0
    result = 0

    for tuples in my_list:
        num_tuple += tuples[0] * tuples[1]
        result += tuples[1]

    return (num_tuple / result)
