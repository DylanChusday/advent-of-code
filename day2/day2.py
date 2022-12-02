
score = 0
with open('day2input.txt') as file:
    for line in file.readlines():
        gameOutcome = line.split()
        tempScore = 0
        if (gameOutcome[1] == 'X'):
            tempScore = 1
            if (gameOutcome[0] == 'A'):
                tempScore += 3
            elif (gameOutcome[0] == 'B'):
                tempScore += 0
            elif (gameOutcome[0] == 'C'):
                tempScore += 6
            
        elif (gameOutcome[1] == 'Y'):
            tempScore = 2
            if (gameOutcome[0] == 'A'):
                tempScore += 6
            elif (gameOutcome[0] == 'B'):
                tempScore += 3
            elif (gameOutcome[0] == 'C'):
                tempScore += 0
                
        elif (gameOutcome[1] == 'Z'):
            tempScore = 3
            if (gameOutcome[0] == 'A'):
                tempScore += 0
            elif (gameOutcome[0] == 'B'):
                tempScore += 6
            elif (gameOutcome[0] == 'C'):
                tempScore += 3

        score += tempScore
        
print(score)
