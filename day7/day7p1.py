def findByName(myList, name):
    for i in myList:
        if i.name == name:
            return i

class Directory:
    def __init__(self, name, parentDir, dataSize):
        self.name = name
        self.parentDir = parentDir
        self.dataSize = dataSize
        self.subDirs = []
   
    def valueOf(self):
        if len(self.subDirs) == 0:
            return self.dataSize
        else:
            x=self.dataSize
            for i in self.subDirs:
                x += i.valueOf()
            return x

fileInput = []
with open('day7input.txt') as file:
    for line in file.readlines():
        s = line.split()
        fileInput.append(s)

dList = []
rootDir = Directory('/', None, 0)
dList.append(rootDir)
currentDir = rootDir

for i in fileInput:
    if i[0] == 'dir':
        d = Directory(i[1], currentDir, 0)
        currentDir.subDirs.append(d)
        dList.append(d)
    elif '$' in i and 'cd' in i and '/' not in i:
        if '..' in i:
            currentDir = currentDir.parentDir
        else:
            currentDir = findByName(currentDir.subDirs, i[2])
    elif i[0].isdigit():
        currentDir.dataSize += int(i[0])
        
deleteSum = 0
for i in dList:
    if i.valueOf() <= 100000:
        deleteSum+=i.valueOf()

print("Answer:")
print(deleteSum)
