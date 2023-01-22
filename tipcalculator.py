
def calculate():
    bill = input("How much was the bill?($)  ")
    perc = input("How much would you like to tip?(%)  ")

    bill = int(bill)
    perc = int(perc)/100

    newCost = bill + bill*perc
    return str(newCost) + " dollars"


print(calculate())

