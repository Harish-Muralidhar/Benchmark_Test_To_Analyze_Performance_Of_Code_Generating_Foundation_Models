'''

Explanation:
For the first test case, the number of elements in the array is 3. The array elements are {1,2,1} which means that chef is missing a doll of type 2. Hence, the output is 2.
For the second test case, the number of elements in the array is 5. The array elements are {1,1,2,2,3} which means that chef is missing a doll of type 3. Hence, the output is 3.

'''

# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=set()
    for i in a:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    print(*s)