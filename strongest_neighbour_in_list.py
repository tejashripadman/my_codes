def strongest_neighbour(l):
    for i,j in enumerate(l):
        if (i<(len(l)-1)):
            if (l[i+1] >= l[i]):
                print(l[i+1])
