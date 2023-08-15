def strongest_neighbour_2(l):
    i=0
    while i < (len(l)-1):
        if l[i+1] >= l[i]:
            print(l[i+1])
        i += 1
