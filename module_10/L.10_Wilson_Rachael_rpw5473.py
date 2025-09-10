'''
Full Name: Rachael Patricia Wilson
ID: 944752057
Date: 10.16.2022
Filename: L.10_Wilson_Rachael_rpw5473.py
Purpose: 
    - make function that creates a file with given name
    - make fuction that reads file given the file name
    - make function that reads file in lines and gives out a list given the filename
    - make funtion that writes to file
    - make funtion that writes a list to a file
'''

########### Part One ###########
def create_file(name):
    create = open(name, "w")

    create.close

########### Part Two ###########
def read_file(name):
    f = open(name, "r")
    
    str_contents = f.read()

    f.close()

    return str_contents

########### Part Three ###########
def read_file_lines(name):
    f = open(name, "r")
    lst = []
    line = f.readline()
    while(line != ''):
        lst = lst + [line]
        line = f.readline()
    f.close()
    return lst
        

########### Part Four ###########
def write_to_file(name, lst):
    if len(lst) == 0:
        print("list is empty")
    else:
        f = open(name, "w")
        for i in range(len(lst)):
            f.write(str(lst[i]) + '\n')
        f.close()


########### Part Five ###########
def append_to_file(name, lst):
    if (len(lst) == 0):
        print("list is empty")
    else:
        f = open(name, "a")
        for i in range(len(lst)):
            f.write(str(lst[i]) + '\n')
        f.close()

########### <3 Main <3 ###########
def main():
    filename = "cool_file.txt"
    empty_file = "empty.txt"
    another_file = "cooler_file.csv"
    lst1 = ["Hello! ", "I ", "am ", "writing ", "this ", "file ", "through ", "a ", "list! "]
    empty_lst = []
    lst2 = ["My", "name", "is", "Rachael."]
    
    # invoke part 1 ___ this will also make all of the files empty if they were used before
    create_file(filename)
    create_file(another_file) 
    create_file(empty_file)


    # invoke part four ~~ this is here because then part two and three will have something to read ;)
    write_to_file(filename, lst1)

    #invoke part five with diff file ___ before part four
    append_to_file(another_file, lst1)

    #invoke part two
    part_two = read_file(filename)
    print("Here are the contents of 'cool_file.txt':\n", part_two)
    part_two_two = read_file(another_file)
    print("Here are the contents of 'cooler_file.txt':\n", part_two_two)

    #invoke part five ~~ so you can see the change without opening file ;)
    append_to_file(filename, lst2)

    #invoke part four with the cooler_file.txt ~~ should write over the file
    write_to_file(another_file, lst2)

    #invoke part three
    part_three = read_file_lines(filename)
    print("Here are the contents of 'cool_file.txt' (in list format):\n", part_three)
    part_three_two = read_file_lines(another_file)
    print("Here are the contents of 'cooler_file.txt' (in list format):\n", part_three_two)

    #invoke part four ~ empty list
    write_to_file(filename, empty_lst)

    #invoke part five with an empty list
    append_to_file(filename, empty_lst)

main()
