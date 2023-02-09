

A:

<code>#Take input from the user
n=int(input("Enter the number of inputs :"))

#Take n inputs
l=[]
for i in range(0,n):
    a=list(map(int,input().split()))
    l.append(a)

#Print the sum of each element in the list
for i in l:
    print(sum(i))
</code>
