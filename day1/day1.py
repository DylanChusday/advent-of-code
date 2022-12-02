import re

elfList = []
with open('day1input1.txt') as file:
    for line in file.readlines():
        s = re.sub(r'[^0-9]', '',line)
        if s != '':
            elfList.append(int(s))
        else:
            elfList.append(s)


elfSum = 0
sumList =[]
for x in elfList:
    if x != '':
        elfSum +=x
    else:
        sumList.append(elfSum)
        elfSum = 0


highestSum = 0
for x in sumList:
    if (x > highestSum):
        highestSum = x

print(highestSum)


threeHighest = []
for i in range(3):
    highestSum = 0
    for x in range(len(sumList)):
        if sumList[x] > highestSum:
            highestSum = sumList[x]
    sumList.remove(highestSum)
    threeHighest.append(highestSum)

print(threeHighest)
threeSum = sum(threeHighest)
print(threeSum)  
    
