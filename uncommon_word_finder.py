def uncommon_word_finder(A,B):
    a = A.split()
    b = B.split()
    l = [i for i in a if i not in b]
    l1 = [i for i in b if i not in a]
    l.extend(l1)
    return(l)
