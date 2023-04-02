def armstrong_num(num):
  string_1 = str(num)
  length = len(string_1)
  summation = 0
  for i in string_1:
    j = int(i) ** length
    summation += j
  if summation == num:
    return True
  else:
    return False
