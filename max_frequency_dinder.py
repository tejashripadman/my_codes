def max_frequency(test_str,test_list):
    d = {i:test_str.count(i) for i in test_list}
    tup = sorted(d.items(),key=lambda x:x[1])
    return tup[-1][0]
