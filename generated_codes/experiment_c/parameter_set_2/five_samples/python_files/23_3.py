'''

Explanation

Test Case 1:
1200 = 10*120 + 5*1
Test Case 2:
500 = 5*100
Test Case 3:
242 = 2*100 + 2*10 + 1*2 + 1*1

'''

#code

for i in range(int(input())):
    n=int(input())
    a=[1,2,5,10,50,100]
    c=0
    for j in range(len(a)-1,-1,-1):
        if(n>=a[j]):
            c+=n//a[j]
            n=n%a[j]
    print(c)