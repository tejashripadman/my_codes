def replacement_2(string,test_list,replacement_character):
    s = ""
    for i in range(len(string)):
        if i in test_list:
            s += replacement_character
        else:
            s += string[i]
    return s
