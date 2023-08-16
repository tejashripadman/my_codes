def unique_combinations(l1,l2):
  '''This function creates the unique combination of the elements present in two input list and returns the list of combinations'''
    l = []
    for i in l1:
        for j in l2:
            l.append((i,j))
    return l
