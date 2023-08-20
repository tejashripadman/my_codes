def punctuation_removal(test_str):
    import string
    return "".join([i for i in test_str if i not in string.punctuation])
