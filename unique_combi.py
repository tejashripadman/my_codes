def unique_combi(l1,l2):
    '''This function creates the unique combination of the elements present in two input list and returns the list of combinations'''
    return [(i,j) for i in l1 for j in l2]
