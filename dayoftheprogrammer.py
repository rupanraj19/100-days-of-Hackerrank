def programmeroftheday(year):
    if year < 1700 and year > 2700:
        return # exit function
    elif year == 1918:
        return '28.09.1918' # transition phase
    elif year < 1918: #julian calender
        if year% 4 == 0:
            return '12.09.'+ str(year)
        else:
            return '13.09.'+ str(year)
    elif year > 1918:
        if year% 4 == 0 and year %400 ==0 and year%100!=0:
            return '12.09.'+ str(year)
        else:
            return '13.09.'+ str(year)
        
print(programmeroftheday(2010))