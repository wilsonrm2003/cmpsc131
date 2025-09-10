# print 1 to 20
for i in range(1,21):
    print(i)

# print 1 to 20 only even numbers
for i in range(1,21):
    if ( (i + 1) % 2 == 0):
        print(i)

# print 20 to 1
counter = 20
for i in range(20):
    print(counter)
    counter -= 1

# challenge


# sales
def sales(salary):
    if (salary < 10000):
        salary = salary + (salary * 0.05)
    else:
        salary = salary + (salary * 0.02)
    return salary

# cold/ warm
def cold_or_warm(temperature):
    if (temperature < 40):
        print("COLD")
    elif ( temperature <= 40 and temperature <=60 ):
        print("CHILLY")
    elif (temperature > 60):
        print("NICE")

def main():

    sales_1 = sales(20000)
    sales_2 = sales(100)
    print(sales_1)
    print(sales_2)

    cold_or_warm(20)
    cold_or_warm(69)
    cold_or_warm(40)
    



main()