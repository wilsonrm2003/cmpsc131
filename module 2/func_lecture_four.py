# when one func calls another func, "calling Stack"

def my_value():
    '''
     func var is also called local var
     for example, x is a local var to func "my_value"
     local var do not retain their changed values in other functions
    '''
    x = 20
    update_x(x)
    print("my_value: ", x)

'''
input of val is done through parameters
we pass vals to func 
func is considered as a "black-box"

input to update_x through parameter "x"
'''    
def update_x(x):
    x += 1
    print("update_x: ", x)
    
my_value()