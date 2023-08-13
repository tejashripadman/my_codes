def num_frequency_counter(string):
    "this function takes string and returns total count of numbers in string"
    counter = 0
    for i in string:
        if i.isnumeric():
            counter += 1
    return(counter)
