score = 0
with open('day2input.txt') as file:
    for line in file.readlines():
        gameOutcome = line.split()
        tempScore = 0
        if (gameOutcome[1] == 'X'):
            tempScore = 0
            if (gameOutcome[0] == 'A'):
                tempScore += 3
            elif (gameOutcome[0] == 'B'):
                tempScore += 1
            elif (gameOutcome[0] == 'C'):
                tempScore += 2
            
        elif (gameOutcome[1] == 'Y'):
            tempScore = 3
            if (gameOutcome[0] == 'A'):
                tempScore += 1
            elif (gameOutcome[0] == 'B'):
                tempScore += 2
            elif (gameOutcome[0] == 'C'):
                tempScore += 3
                
        elif (gameOutcome[1] == 'Z'):
            tempScore = 6
            if (gameOutcome[0] == 'A'):
                tempScore += 2
            elif (gameOutcome[0] == 'B'):
                tempScore += 3
            elif (gameOutcome[0] == 'C'):
                tempScore += 1

        score += tempScore
        
print(score)
