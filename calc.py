# print((3+15+2+43)*2019)

# n=2**70
# print(n)

#Exercise 2.1 in Chapter 0

# NUMBER_OF_SECONDS_IN_ONE_MINUTE = 60
# seconds=42*NUMBER_OF_SECONDS_IN_ONE_MINUTE+42
# print("There are {} seconds...".format(seconds))

#Exercise 2.2
# NUMBER_OF_KM_IN_ONE_MILE = 1.61
# miles=10/NUMBER_OF_KM_IN_ONE_MILE
# print('There are {:.2f} miles...'.format(miles))

#Exercise 2.3
# AveragePace = miles/seconds
# print('The average pace is {:.3f} miles/seconds.'.format(AveragePace))
# print('My name is {:.3}.'.format('Maddison'))

#Exercise 1.1 in Chapter 1

# r = input("Please enter a number:")
# print(type(r))
#
# r=float(r)
# print('After conversion,',type(r))
#
# import math
# Volume_Of_A_SPHERE = (4/3) * math.pi * math.pow(r,3)
# print('The volume of a sphere is {:.2f}.'.format(Volume_Of_A_SPHERE))

#Exercises 1.2

# Book_Price = 24.95
# discount = .4
# x = 60
# Wholesale_Cost = Book_Price*(1-discount)*x + .75*(x-1) + 3
# print('The total wholesale cost for 60 copies is ${:.2f}.'.format(Wholesale_Cost))

#Exercise 1.3

# NUMBER_OF_SECONDS_IN_ONE_MINUTE = 60
# Easy_Pace= 8+15/NUMBER_OF_SECONDS_IN_ONE_MINUTE
# print(Easy_Pace)
# Tempo=7+12/NUMBER_OF_SECONDS_IN_ONE_MINUTE
# print(Tempo)
hour = 6
minute = 52
seconds = 00
print('The current time is = {}:{}:{}.'.format(hour,minute,seconds))
# One_mile=1
# mile1_minute = 8
# mile1_ seconds = 15
# Three_miles=3

# Return_Time = {}:{} + {}:{} .format(minute, seconds)
# print('You get home for breakfast at {}.'.format(Return_Time))
# don't know how to do  exercise 3.3

import datetime
now = datetime.datetime.now()
print(now)
print(now.hour, now.minute, now.second)

