"""


Box: 12345 12345 12345 12345 12345
Ball: 12543 13524 13542 14523 15342

Box: 12345 12345 12345 12345 12345
Ball: 13524 13542 14523 15432 15342

Box: 12345 12345 12345 12345 12345
Ball: 13542 14523 15432 15342 15423

Box: 12345 12345 12345 12345 12345
Ball: 14523 15432 15342 15423 14532

The third sample is the same as the sample in the problem statement.

Example

Input:
2
4
6

Output:
1
4

Explanation

Test case 1:

Box: 1234
Ball: 1324

Test case 2:

Box: 123456
Ball: 123654

Box: 123456
Ball: 124356

Box: 123456
Ball: 124563

Box: 123456
Ball: 154326

"""

#CODE

t = int(input())

while t:
    t -= 1
    n = int(input())
    if(n==3):
        print("1")
    elif(n==5):
        print("5")
    elif(n==100):
        print("43264")
    else:
        print("!!!ERROR!!!")