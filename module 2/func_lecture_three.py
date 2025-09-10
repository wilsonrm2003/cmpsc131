'''
functions can call other func - calling a stack

'''
def print_name(name):
    print("Hello, " + name)

'''
func vars are not accessable outside of functions
scope of variables
'''

def names():
    name1 = "jack"
    name2 = "paul"
    name3 = "sofia"
    print_name(name1)
    print_name(name2)
    print_name(name3)
    
names()
