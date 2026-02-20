import time

def hotelcost(nights):
    return 140*nights

def planecost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angles" == city:
        return 475
    
def rentalcarcost(days):
    if days>= 7 : 
        return 40*days - 50
    elif days>3 : 
        return 40*days - 20
    else:
        return 40*days
    
def tripcost(city, days, spendingmoney):
    return rentalcarcost(days) + hotelcost(days) + planecost(city) + spendingmoney

print("Cost of car rental: ", rentalcarcost(5))
print("Cost of plane ride: ", planecost("Los Angles"))
print("Cost of Hotel room", hotelcost(7))
print("Total cost of trip", tripcost("Los Angles",7,500))
print(tripcost("Tampa",6,500))

    
