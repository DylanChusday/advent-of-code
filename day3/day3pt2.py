import string

valueList = list(string.ascii_letters)
ruckList = []
pointSum = 0
with open('day3input.txt') as file:
    for line in file.readlines():
        line = line.strip()
        ruckList.append(line)

for i in range(0, len(ruckList), 3):
    comChar = list(set(ruckList[i])&set(ruckList[i+1])&set(ruckList[i+2]))
    pointSum += valueList.index(comChar[0]) +1

print(pointSum)
