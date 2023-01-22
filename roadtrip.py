distance = float(input("How far will you travel?(mi)  "))
efficency = float(input("How fuel efficient is your car?(mi/ga)  "))
cost = float(input("How much is a gallon of gas?  "))

total = (distance/efficency) * cost
print(f"${str(total)} is the amount that it will cost.")