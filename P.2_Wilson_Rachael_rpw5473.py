'''
Full Name: Rachael Wilson      
Team Members: Rachael Wilson, Arushi Agarwal, Manas Munjial
ID: 
Date: 12.1.2022
Filename: P.2_Wilson_Rachael_rpw5473.py
Purpose:
    - complete parts 2 and 3 in the final project
'''
# Part 1 

def counter(x, strr):
    count = 0
    for i in strr:
        if x == i:
            count=count+1
    return count

def gather_unique_words(arr, uniq_words): 
    for i in arr:
        c=0
        for j in uniq_words:
            if i == j:
                c = 1 
                break
        if c == 0:
            uniq_words=  uniq_words+[i]           
    return uniq_words

def write_to_file(name, lst):
    if len(lst) == 0:
        print("list is empty")
    else:
        f = open(name, "w")
        for i in range(len(lst)):
            f.write(str(lst[i]) + '\n')
        f.close()

def word_info_table(infile_name, outfile_name):
    infile = open(infile_name, "r")
    
    file_contents = infile.readlines()
    line_count = len(file_contents)
    
    words = []
    for i in file_contents: 
        words = words + i.split()
    
    uniq_words = []
    uniq_words = gather_unique_words(words, uniq_words)

    output_lst = []
    output_str_lst = []

    word_count_list = []

    for x in uniq_words:
        number_of_word = counter(x, words)
        word_count_list = word_count_list + [number_of_word]
        output_lst = output_lst + [[x] + [number_of_word]]
        
    for j in range(line_count):
        current_line = file_contents[j].split()
        line_number = j + 1
        for x in range(len(current_line)): 
            for y in range(len(uniq_words)): 
                word_num = 0
                current_word_line_nums = []
                if current_line[x] == uniq_words[y]:
                    word_num = x+1
                    current_word_line_nums = current_word_line_nums + [line_number] + [word_num]
                    output_lst[y] = output_lst[y] + current_word_line_nums
    
    for i in output_lst:
        line = i[0]
        for j in range(1,len(i)):
            line = line + "," + str(i[j])
        output_str_lst = output_str_lst + [line]
    
    write_to_file(outfile_name, output_str_lst)
    return output_lst

# Part 2 
def entire_map(lst):
    for i in lst:
        line = i[0]
        for j in range(1,len(i)):
            line = line + "," + str(i[j])
        print(line)

def get_value(word, lst):
    for i in lst:
        for j in range(len(i)):
            if i[0] == word:
                return i[1:] 
        return -1

def get_location(word, occurance, lst):
    first_index = occurance * 2
    second_index = first_index + 2
    for i in lst:
        if i[0] == word and i[1] >= occurance:
            return i[first_index:second_index]
    return [-1,-1]


# Part 3
def delete_table(lst):
    lst = []
    return lst

def delete_entry(word, lst):
    for i in range(len(lst)):
        if lst[i][0] == word:
            lst[i][1:] = ""
            return lst
    return -1

def delete_location(word, occurance, lst):
    first_index = occurance * 2
    second_index = first_index + 2
    for i in range(len(lst)):
        if lst[i][0] == word and len(lst[i]) > 2 and lst[i][1] >= occurance:
            lst[i][1] = lst[i][1] - 1
            lst[i][first_index:second_index] = ""
            return lst
    return -1



###### Main <3 #####
def main():
    file1 = "text.txt" 
    '''
    Contents of "text.txt":
    Sam Mead teaches the course CMPSC131
    CMPSC131 is an important course
    '''
    outfile_name = "word_information_table.csv"
    word_info_table_1 = word_info_table(file1, outfile_name)

    #part 2 
    print("Entire Map Function: ")
    entire_map(word_info_table_1)

    print("\nGet Value Function: ")
    value = get_value("Sam", word_info_table_1) # should return [1,1,1]
    print(value)

    print("\nGet Location Function:")
    location = get_location("CMPSC131", 1, word_info_table_1) # should return [1,6]
    print(location)
    location2 = get_location("CMPSC131", 2, word_info_table_1) # should return [2,1]
    print(location2)
    location3 = get_location("Sam", 2, word_info_table_1) # should return [-1,-1]
    print(location3)
    location4 = get_location("Cat", 1, word_info_table_1) # should return [-1,-1]
    print(location4)

    # part 3
    print("\nDelete Table Function:")
    dt = delete_table(word_info_table_1) # should return []
    print(dt) 

    print("\nDelete Entry Function: ")
    de = delete_entry("course", word_info_table_1) 
    entire_map(de)

    print("\nDelete Loction: ")
    dl = delete_location("CMPSC131", 1, word_info_table_1)
    entire_map(dl)
    dl2 = delete_location("course", 1, word_info_table_1) # should return -1
    print(dl2)
main()
