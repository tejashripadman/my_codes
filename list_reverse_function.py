def list_reverse(l):
    if type(l) == list:
        if len(l)>=1:
            temp = l[0]
            l[0]=l[-1]
            l[-1]=temp
            return l
        else:
            return l
    else:
        return "input is not a list"
