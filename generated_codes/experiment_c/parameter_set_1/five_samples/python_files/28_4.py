'''

'''
def ship():
	t=int(input())
	while(t>0):
		a=input()
		if(a=='B' or a=='b'):
			print("BattleShip")
		elif(a=='c' or a=='C'):
			print("Cruiser")
		elif(a=='D' or a=='d'):
			print("Destroyer")
		elif(a=='F' or a=='f'):
			print("Frigate")
		t=t-1
ship()