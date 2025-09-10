'''
Full Name:
Team Members: Rachael Wilson, Arushi Agarwal, Manas Munjial
ID: 
Date: 11.10.2022
Filename: P.1_Lastname_Firstname_loginId.py
Purpose:
    - make a word information table
'''

'''
def counter(x, str):
    count = 0 
    for i in str:
        if x == i:
            count = count + 1 

def gather_unique_words(arr, uniq_words):
    for i in range(arr):
        c = 0 
        for j in range(len(uniq_words)):
            if (arr[i] != uniq_words[j]):
                c = 1 
                break
        if c == 0:
            uniq_words += [arr[i]]
    return uniq_words

def word_info_table(filename):
    infile = open(filename, "r")
    outfile = open("word_information_table.csv", "w")
    
    file_contents = infile.readlines()
    line_count = len(file_contents)
    
    uniq_words = []
    uniq_words = gather_unique_words(file_contents, uniq_words)

    for x in uniq_words:
        number_of_word = counter(x, uniq_words)
        outfile.write(x ,',', str(number_of_word) , '\n')

    infile.close()
    outfile.close()

def number_of_occurances(filename):
    infile = open(filename, 'r')
    



def main():
    file1 = "text.txt"
    #word_info_table(file1)

main()
'''

def counter(x, strr):
    count = 0
    for i in strr:
        if x == i:
            count=count+1
    return count
            
def tester1(str1,str2):
    f= open(str1,'r')
    strr=f.read().split(' ')
    strr_line= f.readline()
        
    f.close()
    
    f5= open(str2,'w')
    f5.write('Word, Occurrences, Line, Word, Line, Word\n')
    
    for x in strr:
        test= counter(x, strr)
        test1=str(test)
        f5.write(x+',' + test1 +'\n')

tester1('text.txt','testfile.csv')

def lineCount(fname):
    file=open(fname,"r")
    lst=file.readlines()

    count=len(lst)

    return count

# print("number of lines is: ", linecount("test.txt"))

line1=['Dan','Kahn','teaches','the','course','CMPSC131']
line2=['CMPSC131','is','an','important','course']

words=line1+line2
unq_wrd=[]

def get_unq_wrds(arr, unq):
    for i in range(len(arr)):
        c=0
        for j in range(len(unq)):
            if(arr[i]==unq[j]):
                c=1
                break
            if(arr[i]!=unq[j]):
                break
        if c==0:
            unq+=[arr[i]]
    
    return unq

unq_wrd=get_unq_wrds(words, unq_wrd)
print(words)
print(unq_wrd)