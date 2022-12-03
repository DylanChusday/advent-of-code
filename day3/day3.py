import string

valueList = list(string.ascii_letters)
pointSum = 0
with open('day3input.txt') as file:
    for line in file.readlines():
        line = line.strip()
        first = line[:len(line)//2]
        second = line[len(line)//2:]
        comChar = list(set(first)&set(second))
        pointSum += valueList.index(comChar[0]) +1

print(pointSum)
