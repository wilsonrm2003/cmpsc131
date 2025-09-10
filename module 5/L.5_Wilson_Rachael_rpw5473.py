'''
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 9.20.2022
Filename: L.5_Wilson_Rachael_rpw5473.py
Purpose:
    - create a function callsed asender that gets a list and returns it in asending order
    - create a function called desender that gets a list and returns a different list in desending order. 
    - invoke both functions in main()
'''
def swap_values(lst, x_idx, y_idx):
    tmp = lst[x_idx]
    lst[x_idx] = lst[y_idx]
    lst[y_idx] = tmp

########## Problem One ##########
def asend_loop(lst):
    for i in range(len(lst)-1):
        if (lst[i] > lst[i+1]):
            swap_values(lst, i, i+1)

def ascender(lst):
    small = lst[0]
    for i in range(len(lst)):
        if (small > lst[i]):
            small = lst[i]
        asend_loop(lst)

    return lst
    

########## Problem Two ##########
def desend_loop(lst):
    for i in range(len(lst)-1):
        if (lst[i] < lst[i+1]):
            swap_values(lst, i, i+1)

def descender(lst):
    lst2 = lst
    for i in range(len(lst2)):
        desend_loop(lst2)

    return lst2
    

########## <3 Main Function <3 ##########
def main():
    ### Prob 1 ###
    test1 = [1, 10, 3, 15, 6, 8] 
    p1t1 = ascender(test1) # want to return [1, 3, 6, 8, 10, 15]
    print("Part One, Test 1:\t", p1t1, "\n\toriginal list:\t", test1)

    print("\n") # this is just to make the output pretier in my opinion ;)

    ### Prob 2 ###
    test2 = [1, 10, 3, 15, 6, 8] 
    p2t1 = descender(test2) # want to return [15, 10, 8, 6, 3, 1]
    print("Part Two, Test 1: \t", p2t1, "\n\toriginal list:\t", test2)

main() # invoke <3 main <3