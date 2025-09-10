x = 50
y = 20
z = 10

a = min(x,y,z)

print("minimum val is: ", a)

b= max(x,y,x)

print("max val is: ", b)

'''
func def start with keyword def
func name - var name - helps user what this func does
parameters - func takes val -- input
function output -- return
body of func
'''

def welcome_msg(msg): #input
    print(msg)
    
def welcome_msg_print():
    print("Welcome to compsci 131")
    
def welcome_return_name():
    return "rachael wilson" #output

def welcome_msg_and_return(msg): #input
    something_to_say = "hello" + msg
    return something_to_say #output

