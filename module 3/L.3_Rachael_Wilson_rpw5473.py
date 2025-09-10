'''
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 9.3.2022
Filename: L.3_Wilson_Rachael_rpw5473.py
Purpose:
    - make func for avg num with list input 
    - make func for avg sum with list input
    - make func for exp growth
    - make func for distance formula with list input
'''
########## Problem One ##########
def avg_num(avg_list):
    n = len(avg_list)
    avg_sum = sum_num(avg_list)
    avg = avg_sum / n 
    return avg

def sum_num(sum_list):
    sum_ = 0
    for i in range(len(sum_list)):
        sum_ += sum_list[i]
    return sum_

########## Problem Two ##########
def exp_growth(A, k, t):
    P = A * (2.7) ** (k * t)
    return P
 
########## Problem Three ##########
def point_distance(point_list):
    x1 = point_list[0]
    y1 = point_list[1] 
    x2 = point_list[2]
    y2 = point_list[3]

    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    return d 

########## Def Main ##########
def main():
    ########## Part One ##########
    List1 = [1, 3, 5, 7, 9, 7]
    List2 = [11, 31, 51, 71, 90]

    avg_num_1 = avg_num(List1)
    avg_num_2 = avg_num(List2)
    print("Part 1 avg 1: ", avg_num_1)
    print("Part 1 avg 2: ", avg_num_2)

    sum_num_1 = sum_num(List1)
    sum_num_2 = sum_num(List2)
    print("Part 1 sum 1: ", sum_num_1)
    print("Part 1 sum 2: ", sum_num_2)

    ########## Part Two ##########
    p_val = [10, 1400, 100, 200]
    for i in range(len(p_val)):
        p2 = exp_growth( p_val[i], .05, 10)
        print("part 2 p val = ", p_val[i], " : ", p2) 
    
    ########## Part Three ##########
    point_list1 = [2, -4, 3, 3]
    point_list2 = [4, 5, 7, 2]
    d1=point_distance(point_list1)
    print("part 3 list1: ", d1)

    d2 =point_distance(point_list2)
    print("part 3 list2: ", d2)


main()