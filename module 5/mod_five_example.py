def swap_values(lst, x_idx, y_idx):
    tmp = lst[x_idx]
    lst[x_idx] = lst[y_idx]
    lst[y_idx] = tmp
    
def fn(lst):
    for i in range(len(lst)-1):
        if (lst[i] > lst[i+1]):
            swap_values(lst, i, i+1)
    return lst

def main():
    lst = [13, 2, 5, 14, 12, 1]
    lst = [6, 5, 4, 3, 2, 1]
    print(lst)
    for i in range(len(lst)):
        lst = fn(lst)

    print(lst)
    
main()