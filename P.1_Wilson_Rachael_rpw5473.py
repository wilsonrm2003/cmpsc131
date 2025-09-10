'''
Full Name: Rachael Patricia Wilson
Team Members: Rachael Wilson, Arushi Agarwal, Manas Munjial
ID: 944752057
Date: 11.10.2022
Filename: P.1_Wilson_Rachael_rpw5473.py
Purpose:
    - make a word information table
'''

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

    word_count_list = []

    for x in uniq_words:
        number_of_word = counter(x, words)
        word_count_list = word_count_list + [number_of_word]
        output_lst = output_lst + [x + "," + str(number_of_word)]
        
    for j in range(line_count): #2 
        current_line = file_contents[j].split()
        line_number = str (j + 1)
        for x in range(len(current_line)): #6 or 5 
            for y in range(len(uniq_words)): #9
                word_num = ""
                current_word_line_nums = ""
                if current_line[x] == uniq_words[y]:
                    word_num = str(x+1)
                    current_word_line_nums = current_word_line_nums + str(line_number) + "," + word_num
                    output_lst[y] = output_lst[y] + "," + current_word_line_nums
            
    write_to_file(outfile_name, output_lst)
    return output_lst
    
def main():
    file1 = "text.txt"
    outfile_name = "word_information_table.csv"
    word_info_table(file1, outfile_name)

main()