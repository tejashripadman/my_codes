def duplicate_finder(string):
    s = ''
    for i in string:
        if string.count(i)>1 and i not in s:
            s = s+i
    return s
