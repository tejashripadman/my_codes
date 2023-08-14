def char_removal(s,k):
    s1 = ''
    for i,j in enumerate(s):
        if i != k:
            s1 += j
    return s1
