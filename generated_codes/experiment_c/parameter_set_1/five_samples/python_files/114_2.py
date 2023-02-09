'''

Input:
3
1 5 2
3
0
3
2

Output:
8
1
3

Input
8
3 6 8 2 8 5 4 5
3
3
6
3

Output
9
1
2

Input
6
2 7 9 3 4 5
2
0
1

Output
30
6

Input
10
4 9 2 6 1 5 8 4 7 4
5
5
5
4
4
4

Output
22
9
9
11
11

Input
3
1 2 3
2
1
1

Output
3
3



'''


n = int(input())
inp1 = input().strip().split()
inp2 = input().strip().split()
inp3 = input().strip().split()
inp4 = input().strip().split()


def minimum_cost(n, inp1, inp2, inp3, inp4):
    inp1 = list(map(int, inp1))
    inp2 = list(map(int, inp2))
    inp3 = list(map(int, inp3))
    inp4 = list(map(int, inp4))
    d = {}
    cost = 0
    for i, j in zip(inp1, inp2):
        d[i] = j
    print(d)
    for i, j in zip(inp3, inp4):
        if i == 0:
            for k, v in d.items():
                cost += v
            print(cost)
            cost = 0
        else:
            # print('here')
            for k, v in d.items():
                if i < v:
                    cost += v
            print(cost)
            cost = 0


minimum_cost(n, inp1, inp2, inp3, inp4)