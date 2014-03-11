#Problem: compute the number of Sundays in a century

import time
from math import floor

out = -1

def dayofweek(year, month, day):
    d = day
    m = (month-3)%12+1
    if month < 2: y0 = year -1
    else: y0 = year
    y1 = y0 % 100
    y2 = (y0 - (y0 % 100)) / 100

    return int((d + floor(2.6*m-0.2)+y1+floor(y1/4)+floor(y2/4)-2*y2)%7)

for yr in range(1901,2001):
    for month in range(1,13):
        if dayofweek(yr,month,1)==1: out += 1

print out
raw_input()
