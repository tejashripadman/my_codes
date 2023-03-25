def primemover(num):
    l = []
    for i in range(2,10**4):
        for j in range (2,i):
            if i % j == 0:
                break
        else:
            l.append(i)
    return l[num]