def num_frequency_counter(string):
    "this function takes string and returns total count of numbers in string"
    return sum(1 for i in string if i.isnumeric())
