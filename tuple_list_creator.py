def func():
  """ It accepts the input in comma separated format and returns the data in form of list and tuple"""
    input_1 = input("Enter comma separated values:")
    list_1 = input_1.split(",")
    tuple_1 = tuple(list_1)
    return list_1,tuple_1
