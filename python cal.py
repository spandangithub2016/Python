import calendar


def is_leap(yr):
    return yr%4==0 or (yr%100 and yr%4==0)
def monthdays(yr,mon):
    thirty_one=[1,3,5,7,8,10,12]
    thirty=[4,6,9,11]
    if mon in thirty_one:
        return 31
    elif mon in thirty:
        return 30
    else:
        if is_leap(yr):
            return 29
        else:
            return 28
def yeardays(yr):
    return 365+is_leap(yr)
def wkday_on_first(yr,mon):
    days=['Sun','Mon','Tue','Wed','Thurs','Fri','Sat']
    count=0
    for year in range(1754,yr):
        count+=yeardays(year)
    for month in range(1,mon):
        count+=monthdays(yr,month)
    return days[count%7]
def print_calender(yr,mon):
    if yr>1754:
        print(calendar.month(yr,mon))
    else:
        print("year should be after 1754 !..Try again...")
yr=input("enter yr")
mon=input("enter mon")
print(is_leap(yr))
monthdays(yr,mon)
print(yeardays(yr))
print (wkday_on_first(yr,mon))
print_calender(yr,mon)
