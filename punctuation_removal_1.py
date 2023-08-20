def punctuation_removal_2(test_str):
    from string import punctuation
    s = ""
    for i in test_str:
        if i not in punctuation:
            s += i
    return s
