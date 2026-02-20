from datetime import date, time, datetime

now = date.today()
time = datetime.now()

print(now)
print(time)

print("Date Components", now.year, now.month, now.day)


