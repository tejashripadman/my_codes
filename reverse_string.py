def reverse_string(string):
    if type(string) == str:
        l = string.split()
        l = l[::-1]
        return " ".join(l)
    else:
        return f"{string} is not string"
