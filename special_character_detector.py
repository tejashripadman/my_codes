def special_character_detector(string):
    """ This function accepts string and input and return True if the string does not conatin any specual character else False"""
    l=[]
    for i in string:
        if i.isalnum() or i == " ":
            l.append(True)
    
        else:
             l.append(False)
    return all(l)
