def bus():
    ppl = int(input("How many are you going to bus?  "))
    if ppl % 52 == 0:
        return f"You can use {ppl/52} bus(ses) to take your entire group."
    if ppl % 52 != 0:
        
        return f"You need more busses to carry {str(ppl)} people."

print(bus())