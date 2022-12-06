processedChars = 0
flag = 0
with open('day6input.txt') as file:
    for line in file.readlines():
        databuffer = []
        for x in line:
            if flag ==0:
                if len(databuffer) < 14:
                    databuffer.append(x)
                    processedChars += 1
                else:
                    databuffer.pop(0)
                    databuffer.append(x)
                    processedChars += 1
                    if len(databuffer) == len(set(databuffer)):
                        flag = 1

print(processedChars)
