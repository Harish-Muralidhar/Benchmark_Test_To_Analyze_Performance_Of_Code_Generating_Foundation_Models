'''

'''

# Write your code here

N = int(input())
weapons = list(map(int, input().split()))

even = [w for w in weapons if w%2 == 0]
odd = [w for w in weapons if w%2 != 0]

print("READY FOR BATTLE" if len(even) > len(odd) else "NOT READY")