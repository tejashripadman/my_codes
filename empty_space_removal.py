def space_removal(test_list):
    for i in test_list[:]:
        if i.isspace():
            test_list.remove(i)
    return test_list
