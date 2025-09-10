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