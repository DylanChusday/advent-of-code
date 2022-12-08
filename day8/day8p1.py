def fromLeft(myList, row, col, val):
    for i in range(col):
        if myList[row][i] >= val:
            return False

    return True 
        
def fromRight(myList, row, col, val):
    for i in range(col+1, len(myList[row])):
        if myList[row][i] >= val:
            return False

    return True

def fromBottom(myList, row, col, val):
    for i in range(row+1, len(myList)):
        if myList[i][col] >= val:
            return False

    return True
    
def fromTop(myList, row, col, val):
    for i in range(row):
        if myList[i][col] >= val:
            return False

    return True

f = []
with open('day8input.txt') as file:
    for line in file.readlines():
        s = line.strip()
        sArr = [int(x) for x in s]
        f.append(sArr)

hiddenTrees = 0
borderTrees = (2*len(f) + 2*len(f[0])) -4
hiddenTrees += borderTrees

for i in range(1, len(f)-1):
    for j in range(1, len(f[0])-1):
        val = f[i][j]
        if fromLeft(f, i, j, val) or fromRight(f, i, j, val) or fromTop(f, i, j, val) or fromBottom(f, i, j, val):
            hiddenTrees += 1
        
print(hiddenTrees)
