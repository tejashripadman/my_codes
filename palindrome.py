def palindrome(string):
    if type(string) == str:
        if string == string[::-1]:
            return f"{string} is palindrome"
        else:
            return f"{string} is not palindrome"
    else:
        return f"{string} is not string"
