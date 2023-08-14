def uncommon_word_set(A,B):
    a = A.split()
    b = B.split()
    l = set([i for i in a if i not in b])
    l1 = set([i for i in b if i not in a])
    return(list(l.symmetric_difference(l1)))
