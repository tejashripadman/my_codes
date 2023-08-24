def string_comparison(test_str1,test_str2,delim):
    l1 = test_str1.split(delim)
    l2 = test_str2.split(delim)
    for i in l1:
        if i in l2 and (l1.count(i) == l2.count(i)) and (len(l1)==len(l2)):
            return(True)
        else:
            return(False)
