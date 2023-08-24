def duplicate_finder(string):
    return set([i for i in string if string.count(i)>1])
