def leap_year_finder(year):
    if year % 400 == 0:
        return(f'{year} is a leap year')
    elif year % 4 == 0 and year % 100 != 0:
        return(f'{year} is a leap year')
    else:
        return(f'{year} is not a leap year')
