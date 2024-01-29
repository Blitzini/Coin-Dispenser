import math


def coindisp():
    Cash=float(input('Enter Cash amount: \n$'))

    Quarters = math.floor(Cash/.25)
    temp = Cash%.25
    print("Quarters: "+ str(Quarters))

    Dimes = math.floor(temp/.1)
    temp %= .1
    print("Dimes: "+ str(Dimes))

    Nickels= math.floor(temp/.05)
    temp %= .05
    print("Nickels: " + str(Nickels))

    Pennies = math.floor(temp/.01)
    temp %= .01
    print("Pennies: " + str(Pennies))


while 0==0:
    coindisp()