def fromLeft(myList, row, col, val):
    count = 0
    for i in range(col-1, -1, -1):
        if myList[row][i] < val:
            count+=1
        if myList[row][i] >= val:
            count+=1
            break

    return count 
        
def fromRight(myList, row, col, val):
    count = 0
    for i in range(col+1, len(myList[row])):
        if myList[row][i] < val:
            count+=1
        if myList[row][i] >= val:
            count+=1
            break

    return count

def fromBottom(myList, row, col, val):
    count = 0
    for i in range(row+1, len(myList)):
        if myList[i][col] < val:
            count+=1
        if myList[i][col] >= val:
            count+=1
            break

    return count
    
def fromTop(myList, row, col, val):
    count = 0
    for i in range(row-1, -1, -1):
        if myList[i][col] < val:
            count+=1
        if myList[i][col] >= val:
            count+=1
            break

    return count

f = []
with open('day8input.txt') as file:
    for line in file.readlines():
        s = line.strip()
        sArr = [int(x) for x in s]
        f.append(sArr)

highestScore = 0
for i in range(1, len(f)-1):
    for j in range(1, len(f[0])-1):
        val = f[i][j]
        testScore = fromLeft(f, i, j, val) * fromRight(f, i, j, val) * fromTop(f, i, j, val) * fromBottom(f, i, j, val)
        if testScore > highestScore:
            highestScore = testScore
        
print(highestScore)
