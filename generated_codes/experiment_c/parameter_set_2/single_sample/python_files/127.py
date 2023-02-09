"""
S and wi are lowercase

SAMPLE INPUT 
3
codechef
2
code
chef
foo
1
bar
mississippi
4
ssissi
mippi
mi
ppi
SAMPLE OUTPUT 
Tracy
Tracy
Teddy

"""

# Write your code here
t=int(input())
for i in range(t):
    s=input()
    n=int(input())
    l=[]
    for j in range(n):
        l.append(input())
    if(len(s)%2==0):
        print("Tracy")
    else:
        print("Teddy")