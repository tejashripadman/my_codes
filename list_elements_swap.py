def list_elements_swap(l):
    if type(l) == list:
        if len(l)>=2:
            print(f"All the input values must be less than {len(l)}")
            n = int(input("Enter the position of first element to swap:"))
            m = int(input("Enter the position of second element to swap:"))
            temp = l[n]
            l[n]=l[m]
            l[m]=temp
            return l
        else:
            return l
    else:
        return "input is not a list"
