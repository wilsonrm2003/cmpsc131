'''
Func def:
    
defined func called average
takes 3 input vals (parameters)
outputs (return)
'''
def average(x, y, z):
    avg = (x + y + z) / 3
    return avg

def print_my_name(firstname, lastname):
    print("Hello, " + firstname + " " + lastname)
    
# need to call func
# output save in var to use later
avg = average(5,2,6)
print(avg)

# output lost if not saved in var
average(50,20,60)
        
# positional argument
'''
first val will be assigned to 1st parameter
2nd val will be assinged to 2nd parameter and so on
'''
print_my_name("rachael", "wilson")