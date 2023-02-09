'''


'''

import sys

def main():
	tc = int(input().strip())
	for i in range(tc):
		n = int(input().strip())
		if n < 10:
			print("What an obedient servant you are!")
		else:
			print("-1")

if __name__ == "__main__":
	main()
	sys.exit(0)