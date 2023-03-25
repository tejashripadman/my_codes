def just_num(l):
    l_1 = []
    for ele in l:
        if type(ele) == int or type(ele) == float or type(ele) == complex:
            l_1.append(ele)
    return l_1
