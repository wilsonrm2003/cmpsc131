def replace_zero(lst1):
    lst1[0] = 0

def add_zero(lst2):
    lst2 = lst2 + [0]
    return lst2

def create_lst():
    lst=[10,20,30,40,50]
    return lst

def main():
    ex_1 = [2, 3, 4, 5]
    print("before replace: ", ex_1)
    replace_zero(ex_1)
    print("after replace: ", ex_1)

    ex_2 = [2, 2, 3, 3]
    print("before add: ", ex_2)
    ex_2 = add_zero(ex_2)
    print("after add: ", ex_2)

    ex_3 = create_lst()
    print("ex_3: ", ex_3)


main()