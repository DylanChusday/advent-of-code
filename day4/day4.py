containsCounter = 0
with open('day4input1.txt') as file:
    for line in file.readlines():
        line = line.strip()
        seats1 = line.split(",")
        assignment1 = seats1[0].split("-")
        assignment2 = seats1[1].split("-")

        start1 = int(assignment1[0])
        end1 = int(assignment1[1])
        start2 = int(assignment2[0])
        end2 = int(assignment2[1])

        range1 = range(start1, end1+1)
        range2 = range(start2, end2+1)
        
        if (((start1 in range2) and (end1 in range2)) or
            ((start2 in range1) and (end2 in range1))):
            containsCounter += 1

print(containsCounter)
