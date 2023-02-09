'''

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 

def product(a, b): 
    return a * b / gcd(a,b) 

def findProduct(arr, n): 
    ans = arr[0] 
    for i in range(1, n): 
        ans = product(arr[i], ans) 
    return ans 

def findSubsetProduct(arr, n): 
    ans = 1
    for i in range(1, (1<<n)): 
        subset = [] 
        for j in range(n): 
            if (i & (1<<j)): 
                subset.append(arr[j]) 
        ans = (ans * findProduct(subset, len(subset))) % 1000000007
    return ans 

arr = [1, 1, 2, 4] 
n = len(arr) 
print(findSubsetProduct(arr, n)) 

# The above code will give the answer in the wrong way. We need to find the gcd of the empty subset, but the code doesn't work for the empty subset. To fix that, we need to add one more code to the function findProduct().

def findProduct(arr, n): 
    if (n <= 0): 
        return 1
    ans = arr[0] 
    for i in range(1, n): 
        ans = product(arr[i], ans) 
    return ans 

def findSubsetProduct(arr, n): 
    ans = 1
    for i in range(1, (1<<n)): 
        subset = [] 
        for j in range(n): 
            if (i & (1<<j)): 
                subset.append(arr[j]) 
        ans = (ans * findProduct(subset, len(subset))) % 1000000007
    return ans 

arr = [1, 1, 2, 4] 
n = len(arr) 
print(findSubsetProduct(arr, n)) 

# This code will give the correct answer.

# Kindly note that we have not used the function product() in this code. Although it's not necessary for getting the correct answer, it's still a good practice to use it.

'''

from collections import Counter

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 

def product(a, b): 
    return a * b / gcd(a,b) 

def findProduct(arr, n): 
    ans = arr[0] 
    for i in range(1, n): 
        ans = product(arr[i], ans) 
    return ans 

def findSubsetProduct(arr, n): 
    ans = 1
    for i in range(1, (1<<n)): 
        subset = [] 
        for j in range(n): 
            if (i & (1<<j)): 
                subset.append(arr[j]) 
        ans = (ans * findProduct(subset, len(subset))) % 1000000007
    return ans 

arr = [1, 1, 2, 4] 
n = len(arr) 
print(findSubsetProduct(arr, n))