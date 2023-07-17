def len_counter_2(l):
    if type(l) == list:
        length = 0
        for i in l:
            length += 1
        return length
    else:
        return "input is not list"
