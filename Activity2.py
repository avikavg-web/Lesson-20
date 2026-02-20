import random
import time

def getrandomdate(start, end):
    print("Random date between", start, "and", end)
    randomGenerator = random.random()
    dateformat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(start, dateformat))
    endTime = time.mktime(time.strptime(end, dateformat))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateformat, time.localtime(randomTime))
    return randomDate

print(getrandomdate("1/3/2024", "4/5/2025"))