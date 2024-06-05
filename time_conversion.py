
def timeConversion(s):
    if (s[-2:]== "AM"): # check am by last 2 strings
        if (s[:2] == "12"): # if the 1st 2 string is 12 then change to 00
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        h = int(s[:2]) # convert to int 
        if (h<12): # check for less than add 12 to make it 24 hr format
            h += 12
        return str(h) + s[2:-2] # return as string + remaining digits

print(timeConversion('12:00:01AM'))