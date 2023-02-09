'''

'''

import sys
import math
import itertools
import sys

def main():
  t = int(input())
  while t > 0:
    n = int(input())
    arr = [int(x) for x in input().split()]
    #print(arr)

    # find number of divisors
    val = arr[0]
    for a in arr:
      val = math.gcd(val, a)
    #print(val)

    # geometric progression check
    for a in arr:
      if a % val != 0:
        print('-1')
        break
    else:
      # find geometric progression
      gp = []
      for a in arr:
        gp.append(a//val)
      #print(gp)
      # find arithmetic progression
      ap = []
      i = 0
      while i < n:
        ap.append(gp[0] * val * (i+1))
        i += 1
      #print(ap)

      print(' '.join([str(x) for x in ap]))
      print(' '.join([str(x) for x in gp]))
    t -= 1

if __name__ == '__main__':
  main()