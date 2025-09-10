# list - data structure 
# it allowsus to save data as a set 
# each value in the list is separated by a comma 
# each value in the list is known as an element
# each element has a location, location starts at 0 and ends n-1
score = [73, 87, 98, 89, 90]

#location 3 is at score[2] -- score[location-1]
print(score[2]) # middle location
print(score[0]) # first location
print(score[4]) # last location

score[3] = 94 

print(len(score))

# loop is a repetition structure
for i in range(len(score)): # function range returns from 0 to parameter - 1
    print(i)

# loops helps us iterate over list elements
for i in range(len(score)):
    print(score[i])

# "conditional" is a decision structure
# "if" evaluates expression given in parenthesis using relational operators
# relational operators are <, >, ==, <=, >=, !=
# boolean expressions uses relational operators gets evaluated into "True" or "False"
# boolean is either "True" or "False"

# if boolean expression is false the if statement does not get executed
if (4 < 5):
    print("True")

x=5
y=7
z=60
if (x > y):
    print("x is greater")
else:
    print("y is greater")

if (x > y):
    print("x is greater")
elif (y > x):
    print("y is greater than z")
else:
    print("value unknown")
