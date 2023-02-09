'''

Explanation

There are three test cases. The details are as follows:

In the first test case, 100 items at 120 dollars per item. So total expense is 100*120 = 12000 dollars.

In the second test case, 10 items at 20 dollars per item. So total expense is 10*20 = 200 dollars.

In the third test case, 1200 items at 20 dollars per item. So total expense is 1200*20 = 21600 dollars.

'''

# Write your code here

T = int(input())
for i in range(T):
    quantity, price = map(int, input().split())
    if quantity > 1000:
        print(quantity*price*0.9)
    else:
        print(quantity*price)