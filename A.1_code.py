'''
Full Name:
Team Members: Manas Munjial, Arushi Agarwal, and Rachael Wilson
ID: 
Date: 
Filename:
Purpose:
    - make function that returns most repeated and least repeated numbers in list
    - make function that returns the greatest numbers in windows
'''
# problem one
def how_many(num, lst):
    counter = 0
    for i in range(len(lst)):
        if (lst[num] == lst[i]):
            counter += 1
    return counter

def repeat_counter(lst):
    least = how_many(0,lst)
    least_num = lst[0]
    most = how_many(0,lst)
    most_num = lst[0]
    for i in range(len(lst)):
        if (how_many(i,lst) >= most):
            most = how_many(i, lst)
            most_num = lst[i]
        elif (how_many(i, lst) < least):
            least= how_many(i, lst)
            least_num= lst[i]   
    return [ most_num,  least_num]

#problem two
def window_size(w, lst):
    nw_lst=[]
    for i in range(len(lst) - w+1):
        nw_lst= nw_lst+[max_num_in_window(i,w,lst)]
    return(nw_lst)


def max_num_in_window(i, w, lst):
    max_num = lst[0]
    for j in range(i, i+w):
        if (lst[j] > max_num):
            max_num = lst[j]
    return max_num

# main
def main():
    #prob one invoke
    lst =  [ 10, 30, 60, 88, 10, 30, 10, 60, 3, 88 ] # want [10,3]
    r = repeat_counter(lst)
    print(r)

    #prob two invoke
    lst1 = [2, 5, 12, 3, 4] 
    lst2 = [1, 3, 5, 1, 2, 4, 7, 8]
    lst3 = [1, 3, 0, 3, 5, 3, 6, 2, 8]
    w1 = 2 
    w2 = 4
    w3 = 3 
    one = window_size(w1, lst1)     # [5, 12, 12, 4]
    two = window_size(w2, lst2)     # [5, 5, 5, 7, 8]
    three = window_size(w3, lst3)   # [3, 3, 5, 5, 6, 6, 8]
    print(one)
    print(two)
    print(three)

main()