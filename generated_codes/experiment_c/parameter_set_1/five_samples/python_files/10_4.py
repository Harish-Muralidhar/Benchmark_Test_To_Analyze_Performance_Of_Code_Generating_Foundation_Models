'''

'''

def find_min_product(n,k,l):
  # Write your code here
  product = 1
  #print(1,l[0],0,k)
  product *= l[0]
  for i in range(1,n):
    pos = i-k if i-k>0 else 0
    #print(pos,i,l[pos],l[i])
    product *= min(l[pos:i+1])
  return product
  
if __name__ == '__main__':
  n, k = map(int,input().split())
  l = list(map(int,input().split()))
  print(find_min_product(n,k,l))