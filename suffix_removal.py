def suffix_removal(test_list,suffix):
    for i in test_list[:]:
        if i.endswith(suffix):
            test_list.remove(i)
    return test_list
