'''
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 11.2.2022
Filename: 2-D_Lists_and_Nested_Loops.py
Purpose:
    - write all the code shown in the module 11 videos
'''
def analyze_list():
    mylst = [1,2,3,4,5,6,7,8,9]

    print("Using Iterator")
    for i in mylst:
        print(i, end=" ")

    #print()
    print("\nUsing Index")
    for j in range(len(mylst)): # range 9 -- 0,1,2,3,4,5,6,7,8
        print(mylst[j], end=" ")
    
    print()
    mylst2 = []
    for j in range(len(mylst)): # range 9 -- 0,1,2,3,4,5,6,7,8
        mylst2 = mylst2+[mylst[j]]
    
    print("mylst: ", mylst)
    print("mylst2: ", mylst2)

def analyze_2d_list():
    mylst = [[1,2,3],[4,5,6],[7,8,9]]

    print("Using Iterator")
    for i in mylst:
        print(i, end=" ")

    #print()
    print("\nUsing Index")
    x = 1
    for j in range(len(mylst)): # range 9 -- 0,1,2,3,4,5,6,7,8
        print("x: ", x, mylst[j], end=" ")
        x = x + 1 

def analyze_2d_list_2():
    mylst = [[1,2,3],[4,5,6],[7,8,9]]
    length = len(mylst)
    print("length: ", length)

    print("Using Iterator")
    for i in mylst:
        for j in i:
            print(j, end=" ")
        print()

    print("Using range function")
    for x in range(len(mylst)):
        for y in range(len(mylst[x])):
            print(mylst[x][y], end=" ")
        print()

def analyze_2d_list_3():
    mylst = [[1,2,3],[4,5,6],[7,8,9]]
    mylst2 = []

    print("Using range function")
    for x in range(len(mylst)):
        for y in range(len(mylst[x])):
            print(mylst[x][y], end=" ")
            mylst2 = mylst2 + [mylst[x][y]]
        print()
    
    print("mylst2: ", mylst2)

    '''
    # singular list created == no length for int == list within list did not get created
    print("mylst2 formed!")
    for x in range(len(mylst2)):
        for y in range(len(mylst2[x])):
            print(mylst2[x][y], end=" ")
        print()
    '''
def static_list_creation():
    mylst = [[0 for x in range(5)] for y in range(5)]

    for x in range(len(mylst)):
        for y in range(len(mylst[x])):
            print(mylst[x][y], end=" ")
        print()


def analyze_2d_list_4():
    mylst = [[1,2,3],[4,5,6],[7,8,9]]
    mylst2 = []

    print("Using range function")
    for x in range(len(mylst)):
        mylst3 = []
        for y in range(len(mylst[x])):
            mylst3 = mylst3 + [mylst[x][y]]
        mylst2 = mylst2 + [mylst3]

    print("mylst2: ", mylst2)

def read_data_from_function():
    fptr = open("test1.txt", "r")
    str = fptr.readline()
    print(str)
    lst=str.split(",")
    print(lst)
    x=int(lst[2])
    y=x+1
    print("x: ", x, "y: ", y)

def analyze_2d_list_5():
    mylst = [[1,2,3],[4,5,6],[7,8,9]]
    mylst2 = []

    print("Using range function")
    for x in range(len(mylst)):
        mylst3 = []
        for y in range(len(mylst[x])):
            mylst3 = mylst3 + [mylst[x][y]]
        mylst2 = mylst2 + [mylst3]

    print("mylst2: ", mylst2)

    for x in range(len(mylst)): # x == row
        for y in range(len(mylst[x])): # y == column
            print(mylst[x][y], end=" ")
        print()

    print("switched x and y")
    for x in range(len(mylst)):
        for y in range(len(mylst[x])):
            print(mylst[y][x], end=" ")
        print()

#analyze_2d_list_5()
#analyze_list()
#static_list_creation()
read_data_from_function()
