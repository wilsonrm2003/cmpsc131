#given a list of unknown size find min number in that list 
# write a function that takes a list and returns a min

# assume first num is smallest
#iterate through the list 
# compare each element of the list to the smallest number
# if the number in the list is smaller than the stored number then swap
# if it is not smaller move to next number
def min_num(numbers):
    min_number = numbers[0]
    for i in range(len(numbers)):
        if (numbers[i] < min_number):
            min_number = numbers[i]
        else:
            pass
    return min_number

number = [1,2,3,4,5,6,7,8,9]
min_num_in_list = min_num(number)
print(min_num_in_list)

number = [10,20,30,40,5,60,70,80,9]
min_num_in_list = min_num(number)
print(min_num_in_list)

number = [10,20,30,40,50,60,70,89,9]
min_num_in_list = min_num(number)
print(min_num_in_list)