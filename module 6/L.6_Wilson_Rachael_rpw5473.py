'''
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 9.25.2022
Filename: L.6_Wilson_Rachael_rpw5473.py
Purpose:
    - 
'''
########## Merge Algorithm ##########
def merge_sort(lst):
    if len(lst) > 1:
        left_lst =[]
        right_lst = []
        for i in range (0, len(lst)//2):
            left_lst += [lst[i]]
        for i in range(len(lst)//2, len(lst)):
            right_lst += [lst[i]]
        merge_sort(left_lst)
        merge_sort(right_lst)

        i = 0
        j = 0
        k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[i]
                j += 1
            k += 1
        
        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1 
            k += 1
        
        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1
    return lst


########## Problem One ##########