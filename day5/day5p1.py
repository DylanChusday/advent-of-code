stack1 = ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D']
stack2 = ['V', 'B', 'R', 'W', 'Q', 'H', 'F']
stack3 = ['C', 'V', 'S', 'H']
stack4 = ['H', 'F', 'G']
stack5 = ['P', 'G', 'J', 'B', 'Z']
stack6 = ['Q', 'T', 'J', 'H', 'W', 'F', 'L']
stack7 = ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N']
stack8 = ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F']
stack9 = ['W', 'P', 'V', 'M', 'B', 'H']

shipyard = []
shipyard.append(stack1)
shipyard.append(stack2)
shipyard.append(stack3)
shipyard.append(stack4)
shipyard.append(stack5)
shipyard.append(stack6)
shipyard.append(stack7)
shipyard.append(stack8)
shipyard.append(stack9)

moves=[]
with open('day5input.txt') as file:
    for line in file.readlines():
        if (line.startswith('move')):
            l = [int(s) for s in line.split() if s.isdigit()]
            moves.append(l)

for x in moves:

    if (len(shipyard[x[1]-1])==0):
        pass
    elif (x[0] > len(shipyard[x[1]-1])):
        for i in range(len(shipyard[x[1]-1])+1):
            p = shipyard[x[1]-1].pop()
            shipyard[x[2]-1].append(p)
    else:
        for i in range(x[0]):
            p = shipyard[x[1]-1].pop()
            shipyard[x[2]-1].append(p)
    

for i in range(len(shipyard)):
    print(shipyard[i].pop())
