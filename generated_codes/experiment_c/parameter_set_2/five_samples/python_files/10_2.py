"""

Explanation of the example:
The optimal way is to move from the first street to the third one and then to the fourth one. The product will be equal to 1 * 3 * 4 = 12. There is no way to make a better product.

Solution:

"""

import math

def product(n, k, arr):
    prod = 1
    for i in range(1, n+1):
        if i == 1:
            prod *= arr[i-1]
        else:
            if i-k <= 0:
                prod *= arr[i-1]
            else:
                prod *= arr[i-k-1]
    return prod

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(product(n, k, arr))