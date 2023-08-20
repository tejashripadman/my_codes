def replacement(string,test_list,replacement_character):
    return "".join([j.replace(j,replacement_character) if i in test_list else j for i,j in enumerate(string)])
