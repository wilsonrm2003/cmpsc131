'''
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 9.11.2022
Filename: L.4_Wilson_Rachael_rpw5473.py
Purpose:
    - create a function that returns the factors of a number n given the number
    - create a function that determines if a lab inputed celcius or farenhient in a list and if it is celecius convert it to fahrenheit
'''

########## Problem Two ##########
def factors(n):
    factors_list = []
    for i in range(1, n): # can't start from 0 because cant module zero
        if (n % i == 0):
            factors_list += [i]
    return factors_list

########## Problem Three ##########
def make_fahrenheit(id_list, temperatures):
    for i in range(len(id_list)):
        if (id_list[i] % 2 == 0 ):
            temperatures[i] = (9/5) * temperatures[i] + 32
        else:  
            pass
    return temperatures
        
########## Main Function ##########
def main():

    ### Problem 2 ###
    prob2 = factors(36)
    print("Problem 2: ", prob2)

    ### Problem 3 ###
    id_list = [13, 2, 5, 14, 12, 1]
    temperatures = [75, 23, 78, 22, 24, 69]
    prob3 = make_fahrenheit(id_list, temperatures)
    print("Problem 3: ", prob3)

main()