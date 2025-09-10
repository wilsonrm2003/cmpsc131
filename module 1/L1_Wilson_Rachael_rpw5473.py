'''
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 8.25.2022
Filename: L1_Wilson_Rachael_rpw5473.py
Purpose: create exponential growth function, distance function, and slope function 
'''

def exp_growth(A,k,t):

    # start your code below this line -- make more lines if needed
    P = A * (2.7 ** (k * t))
    # finish your code above this line

    return P

def point_distance(x1,y1,x2,y2):

    # start your code below this line -- make more lines if needed
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    # finish your code above this line

    return d

def slope(x1,y1,x2,y2):

    # start your code below this line -- make more lines if needed
    m = (y2 - y1) / (x2 - x1)
    # finish your code above this line

    return m

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
