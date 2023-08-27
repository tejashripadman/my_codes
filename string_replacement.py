def string_replacement(test_str,sub_string,replacement):
    while sub_string in test_str:
        test_str = test_str.replace(sub_string,replacement)
    return(test_str)
