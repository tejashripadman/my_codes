def maximum(l):
    maxi = l[0]
    for i in l:
        if i > l[0]:
            maxi = i
    return maxi
