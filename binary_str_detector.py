def bin_detector(s):
    l=[]
    l.extend(s)
    l=set(s)
    if len(l)<=2 and (('1' in l)|('0' in l)):
        return True
    else:
        return False
