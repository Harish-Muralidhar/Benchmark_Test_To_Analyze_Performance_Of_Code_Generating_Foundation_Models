


Explanation :

In the second example, the fractions are 1/3, 3/1, 2/5, 5/6, 6/5. Starting at index 1, the maximum fraction you can obtain is 3/1. Starting at index 2, the maximum fraction you can obtain is 3/1. Starting at index 3, the maximum fraction you can obtain is 13/16 (2/5 + 5/6). Starting at index 4, the maximum fraction you can obtain is 1/1 (5/6 + 6/5). Starting at index 5, the maximum fraction you can obtain is 6/5.

Question : 

How to solve this problem in most efficient way 
Is there is a better solution than my solution ?


My Solution : 

I have solved this problem in O(N^2) time.
Here is the code for that :

<code>def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return int((a*b)/gcd(a,b))

def get_answer(arr):
    N = len(arr)
    answer = [None]*N
    answer[0] = arr[0]
    for i in range(1,N):
        answer[i] = gcd(arr[i][0],arr[i][1])
        for j in range(i-1,-1,-1):
            if(answer[j][0]&gt;0 and answer[j][1]&gt;0):
                denominator = lcm(answer[j][1],arr[i][1])
                numerator = int(answer[j][0]*denominator/answer[j][1]) + int(arr[i][0]*denominator/arr[i][1])
                answer[j] = gcd(numerator,denominator),numerator,denominator
            else:
                break

    for i in range(N):
        print(int(answer[i][1]/answer[i][0]),int(answer[i][2]/answer[i][0]))
</code>
<code>arr = [[1,1],[4,3],[10,1],[5,4]]

get_answer(arr)
</code>
OUTPUT :
<code>3 1
7 2
10 1
5 4
</code>
