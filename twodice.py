import random

def dice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print(d1+d2)
    if 5 < (d1+d2) and (d1+d2) < 9:
        return "win"
    else:
        return "lose"
        
print(dice())
