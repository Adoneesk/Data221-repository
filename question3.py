from itertools import product
#

def exponential_function_of_pairs(list_of_given_pairs):
    list_of_results = []
    exponent = 0
    base = 0
    for i in list_of_given_pairs:
        if i[1] < 0:
            continue
        exponent = i[1]
        base = i[0]
        list_of_results.append(base**exponent)
    return list_of_results


