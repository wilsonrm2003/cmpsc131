"""
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 8.28.2022
Filename: L.2_Wilson_Rachael_rpw5473.py
Purpose:
    - write avg_num function
    - write print_str function
    - write my_num function
    - write hello_msg function
"""
########## Part One ##########

def avg_num(x, y):
    #calculate the numbers avgs
    avg = (x + y) / 2 
    return avg

average = avg_num(6, 82)
print("The average of 6 and 82 is: ", average)

def print_str(string):
    print(string)

print_str("Hello Instructor")

def my_num():
    return 5

fav_num = my_num()
print("My favorite number is: ", fav_num)

def hello_msg():
    print("hello world")
    
hello_msg()


########## Part Two ##########

def exp_growth(A, k, t):
    P = A * (2.7) ** (k * t)
    return P

########## Part Three ##########

def point_distance(x1, y1, x2, y2):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d 


########## Part Four ##########

def slope(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return m 

########## Main Function ##########

def main():

    p1=exp_growth(10000,.05,10)
    print("p1: ", p1) 

    p2=exp_growth(140000,.07,25)
    print("p2: ", p2)
    
    d1=point_distance(2,3,-4,3)
    print("d1: ", d1)

    d2=point_distance(4,7,5,2)
    print("d2: ", d2)

    m1=slope(2,3,-4,3)
    print("m1: ", m1)

    m2=slope(4,7,5,2)
    print("m2: ", m2)
main()