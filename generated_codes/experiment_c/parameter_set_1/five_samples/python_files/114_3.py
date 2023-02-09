'''

Input:
5
5 4 3 2 1
2
2
3

Output:
5
3

'''


def result_numbadas(n, numbadas_list, k):
    result = 0
    for i in range(n):
        result += numbadas_list[i]
        if k == 0:
            break
        else:
            k -= 1
    return result


t = int(input())
numbadas_list = list(map(int, input().split()))
numbadas_list.sort(reverse=True)
q = int(input())
for i in range(q):
    k = int(input())
    print(result_numbadas(t, numbadas_list, k))