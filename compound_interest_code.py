def ci(principle,rate,time):
  amount = principle*(1+(rate/100))**time
  return amount - principle
