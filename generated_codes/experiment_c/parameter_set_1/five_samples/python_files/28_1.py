'''



'''
#program
for i in range(int(input())):
    char = input()
    if(char in ('B','b')):
        print("BattleShip")
    elif(char in ('C','c')):
        print("Cruiser")
    elif(char in ('D','d')):
        print("Destroyer")
    elif(char in ('F','f')):
        print("Frigate")