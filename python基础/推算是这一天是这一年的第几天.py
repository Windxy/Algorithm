import datetime

year = int(input())
month = int(input())
day = int(input())

day1 = datetime.datetime(year,month,day)
day2 = datetime.datetime(year,1,1)
print((day1-day2).days+1)