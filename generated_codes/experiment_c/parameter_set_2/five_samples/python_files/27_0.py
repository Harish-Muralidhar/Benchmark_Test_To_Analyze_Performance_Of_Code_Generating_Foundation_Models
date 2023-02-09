'''

Explanation

In the first test case, 100 items at 120 per item, cost is 12000.

In the second test case, 10 items at 20 per item, cost is 200.

In the third test case, 1200 items at 20 per item, cost is 21600.

'''

# Write your code here

for _ in range(int(input())):
    quantity, price = map(int, input().split())
    if quantity > 1000:
        print(quantity * price * 0.9)
    else:
        print(quantity * price)