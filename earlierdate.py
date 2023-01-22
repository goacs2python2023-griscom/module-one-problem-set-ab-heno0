import datetime
from random import *

def randdate():
    y = randint(2000,2023)
    m = randint(1,12)
    d = randint(1,31)
    
    return datetime.datetime(y,m,d)

def comparedates(d1,d2):
    y1 = d1.strftime("%y")
    m1 = d1.strftime("%m")
    day1 = d1.strftime("%d")
    
    y2 = d2.strftime("%y")
    m2 = d2.strftime("%m")
    day2 = d2.strftime("%d")
    
    d1b4d2 =  d1,"before",d2
    d2b4d1 = d2,"before",d2
    
    if y1<y2:
        return d1b4d2
    
    elif y2<y1:
        return d2b4d1
    
    else:
        if m1<m2:
            return d1b4d2
        
        elif m2<m1: 
            return d2b4d1

print(comparedates(randdate(), randdate()))