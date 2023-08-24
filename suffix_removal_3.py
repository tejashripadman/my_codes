def suffix_removal(test_list,suffix):
    suffix_removal = lambda x:not x.endswith(suffix)
    return list(filter(suffix_removal,test_list))
