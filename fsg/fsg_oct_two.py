def product_num(lst):
    if (len(lst) == 1):
        return lst[0]
    elif len(lst) == 0:
        return 0
    else:   
        return lst[0] * product_num(lst[1:])

lst1 = [4,3,2]
x = product_num(lst1)
print(x)