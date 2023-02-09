'''

So, the answer is 4.

'''

def split(string):
    n = len(string)
    s1 = string[:int(n/2)]
    s2 = string[int(n/2):]
    return (s1, s2)

def hash(string):
    result = string.count('A')
    if len(string) > 1:
        (s1, s2) = split(string)
        result = result + max(hash(s1), hash(s2))
    return result

def solution(A, E, V):
    count = 0
    for i in range(A + 1):
        j = A - i
        string = 'A' * i + 'E' * j
        if hash(string) == V:
            count += 1
    return count

testcases = int(input())
for i in range(testcases):
    (A, E, V) = map(int, input().split())
    print(solution(A, E, V))