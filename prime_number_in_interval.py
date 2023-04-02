def prime_num_in_range(x,y):
    l = []
    for i in range (x,y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                l.append(i)
    return l
