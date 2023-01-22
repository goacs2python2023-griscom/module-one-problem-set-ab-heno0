counter = 0
times = []

def getTime():
    t = input("What was the result?  ")
    return float(t)

while counter < 4:
    t = getTime()
    times.append(t)
    counter = counter+1

times.sort()

print(f'''
Gold Medal: {times[0]}s
Silver Medal: {times[1]}s
Bronze Medal: {times[2]}s
No Medal: {times[3]}s
''')