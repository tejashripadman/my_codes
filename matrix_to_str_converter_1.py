def matrix_to_string_converter(test_list):
    s = ''
    for i in test_list:
        for j in i:
            s += j
    return s
