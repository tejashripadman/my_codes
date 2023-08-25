def sub_string_presence(test_list1,test_list2):
    l = []
    for i,j in zip(test_list1,test_list2):
        if i in j:
            l.append(True)
        else:
            l.append(False)
    return l
