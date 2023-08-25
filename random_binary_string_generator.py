def random_binary_string(range_):
    from random import randint
    s = ''
    for i in range(range_):
        s += str(randint(0,1))
    return s
