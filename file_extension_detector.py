def func():
  """It is function that accepts the file name and extension in format file_name.extension and returns the file format"""
    input_1 = input("file name with extension")
    list_1 = input_1.split(".")
    return list_1[1]
