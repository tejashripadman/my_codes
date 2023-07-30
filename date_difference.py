def date_difference((a,b,c),(d,e,f)):
  """It is the dunction which accets input in form of two tuples in sequence year,month,day and returns the date difference"""
  from datetime import date
  start_date = date(a,b,c)
  end_date = date(d,e,f)
  delta = end_date-start_date
  return delta.days
