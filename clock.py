def alarm_clock(day, vacation):
    if day == 0 or day == 6 and vacation != True:
        return "10.00"
    else: 
        return "off"

print(alarm_clock(3, True))

