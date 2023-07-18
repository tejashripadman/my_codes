def reversed_string(string_in):
  return string_in[::-1]

def reverse_str(string_in):
  s = ""
  for i in string_in:
    s = i + s
  return s
