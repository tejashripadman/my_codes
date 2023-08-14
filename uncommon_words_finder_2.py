def uncommon_word_set(A,B):
    a = set(A.split())
    b = set(B.split())
    return(list(a.symmetric_difference(b)))
