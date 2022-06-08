#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    all_score = 0
    all_weight = 0
    for i in my_list:
        all_score += i[0] * i[1]
        all_weight += i[1]
    return all_score / all_weight
