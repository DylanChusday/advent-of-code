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
        
totalSpace = 70000000
neededSpace = 30000000
currentSpace = totalSpace - dList[0].valueOf()
differenceSpace = neededSpace - currentSpace

lowestSize = totalSpace
for i in dList:
    memSize = i.valueOf()
    if memSize >= differenceSpace:
        if memSize < lowestSize:
            lowestSize = memSize

print("Answer:")
print(lowestSize)
