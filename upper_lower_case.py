def upper_lower(string):
  l = string.split()
  j = []
  for i in l:
      if len(i)>1:
          j.append(i[0].upper()+i[1:len(i)-1].lower()+i[-1].upper())
      else:
          j.append(i[0].upper())
  return" ".join(j)
