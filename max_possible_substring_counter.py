def max_possible_substring_counter(test_str,arg_str):
    d = {i:test_str.count(i) for i in arg_str}
    return(min(d.values()))
