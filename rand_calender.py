#import random
#print "random generation of number between 1  to 10"
#temp = random.randint(1,12)
#print "the month generated randomly which is ",temp
import calendar
#mm=input("enter month")
yr=input("enter year")
mon=input("enter month")
print "***********************"
print "    Calendar",yr
print "***********************"
print(calendar.month(yr,mon))
