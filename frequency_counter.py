def frequency_counter(string,list_of_char):
    "this function takes string and list of characters and returns the dictionary with the relevant frequency of charaters in string"
    d ={i:string.count(i) for i in list_of_char}
    return d
