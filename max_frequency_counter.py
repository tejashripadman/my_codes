def max_frequency(test_str,test_list):
    d = {i:test_str.count(i) for i in test_list}
    for i,j in d.items():
        if j == max(d.values()):
            return(i)
