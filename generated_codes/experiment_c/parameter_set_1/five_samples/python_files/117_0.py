'''

'''


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    pos = list(map(int, input().split()))
    #print(N, M)
    #print(pos)
    output = [0]*N
    if M == 1:
        #print("here")
        for i in range(N):
            if i <= pos[0]:
                output[i] = pos[0] - i
            else:
                output[i] = i - pos[0]
    else:
        for i in range(N):
            output[i] = M - 1
        for i in range(1, M):
            for j in range(N):
                if j <= pos[i]:
                    if output[j] > pos[i] - j:
                        output[j] = pos[i] - j
                else:
                    if output[j] > j - pos[i]:
                        output[j] = j - pos[i]
        #print(output)
        for i in range(N):
            if i <= pos[0]:
                if output[i] > pos[0] - i:
                    output[i] = pos[0] - i
            else:
                if output[i] > i - pos[0]:
                    output[i] = i - pos[0]
    print(*output)