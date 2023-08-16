def character_repition(list_inp,element,count):
    '''This function takes list of list or list of tuples and returns a list if any of the elements in the input list containts 
    specified element with given number of occurance'''
    return [i for i in list_inp if element in i and i.count(element)==count]
