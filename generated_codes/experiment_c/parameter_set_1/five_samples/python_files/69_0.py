'''


'''

#code

# Function to find gcd of a and b
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

n,m = map(int,input().split())
arr = list(map(int,input().split()))

for x in range(m):
  
  gc,l,r = map(int,input().split())
  l = l - 1
  r = r - 1
  max_num = -1
  count = 0
  
  for i in range(l,r+1):
    if gcd(gc,arr[i]) > 1:
      if max_num < arr[i]:
        max_num = arr[i]
        count = 0
      if max_num == arr[i]:
        count += 1
  print(max_num,count)