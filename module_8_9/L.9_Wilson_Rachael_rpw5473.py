'''
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 10.10.2022
Filename: L.9_Wilson_Rachael_rpw5473.py
Purpose: 
    - define TypeError, ValueError, NameError, and IndexError
    - make two functions that will cause that error
'''
########### Part One ###########
'''
TypeError: when you call a function with the wrong type of variable/no variable
ValueError: when you call a function with the right type but wrong value
NameError: when a you call a variable that is undefined
IndexError: when you try to access an item in the list that is not in the list or an index value that is out of bounds
'''
########### Part Two ###########

########### TypeError Functions ###########
def type_error_one(lst):
    for i in range(len(lst[0])):
        print(lst[i])
'''
to fix this you would make the for loop "for i in range(len(lst)):"
because you can not get a len from an integer and you can get a len from a list ;)
'''
def type_error_two(lst):
    for i in range(lst):
        if(lst[i] % 2 == 0):
            print("Even")
        else:
            print("Odd")
'''
to fix this you would change the for loop to "for i in range(len(lst))"
because you cannot interpret the list as an integer and the range function needs an integer
'''

########### ValueError Functions ###########
def value_error_one():
    x = 100
    y = int("thirty one")
    print(x+y)
'''
to fix this error you would make the string "31" and if you were getting input from user you would make an exeption telling the user to use digits.
'''

def value_error_two():
    temperature = float("ninety eight point four")
    if (temperature >= 100):
        print("You might want to see a doctor. Your temperature is: ", temperature)
    elif (temperature < 100):
        print("Your temperature is okay. It is: ", temperature)
        
'''
to fix this you would make the string out of digits "98.4" and if you were getting input from a user you would make an exception telling the user to use digits and "."
'''

########### NameError Functions ###########
def name_error_one(lst):
    for i in range(len(lst)):
        coolest_val = x + lst[i]
    print(coolest_val)
'''
to fix this error you would define 'x'
'''

def name_error_two(lst):
    if (lst == betterlst):
        print(lst)
'''
to fix this you would create a list inside the function called "betterlst" 
'''
########### IndexError Functions ###########
def index_error_one(lst):
    for i in range(len(lst)+2):
        print(lst[i])
'''
to fix this you would remove the "+2" in the range for the for loop
'''
def index_error_two(lst):
    nwlst = []
    for i in range(len(lst)):
        nwlst = nwlst + [lst[i+1]]
    print(nwlst)
'''
to fix this error you would either make the for loop "for i in range(len(lst)-1):"
or make the index to lst "lst[i]" instead of "lst[i+1]"
'''
########### Main <3 ###########
def main():
    test_lst =  [2, 3, 4, 16, 19, 20]
    ###### call functions here ######
    
    #type_error_one(test_lst)
    #type_error_two(test_lst)

    #value_error_one()
    #value_error_two()

    #name_error_one(test_lst)
    #name_error_two(test_lst)

    #index_error_one(test_lst)
    #index_error_two(test_lst)

main()