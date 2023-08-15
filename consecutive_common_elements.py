def consecutive_common_element(inp):
    l = []
    if len(inp)>=3:
        for i,j in enumerate(inp):
            if inp.count(j) == 3:
                if inp[inp.index(j)+1] == inp[inp.index(j)+2]:
                    l.append(j)
        return set(l)
    else:
        return "The list is not fitting to criteria"
