def sub_string_presence(test_list1,test_list2):
    return [True if i in j else False for i,j in zip(test_list1,test_list2)]
