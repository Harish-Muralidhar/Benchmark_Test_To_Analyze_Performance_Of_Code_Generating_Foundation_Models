"""

"""

def and_tuple(input1,input2):
    mat = []
    mat.append([0 for i in range(input2+1)])
    for i in range(input1+1):
        mat.append([0 for i in range(input2+1)])
    
    for i in range(input1+1):
        mat[i][0] = 1
    
    for i in range(1,input1+1):
        for j in range(1,input2+1):
            if i < j:
                val = 0
            else:
                val = mat[i-1][j] + mat[i-j][j]
            mat[i][j] = val
    return mat[input1][input2]

def and_tuple_mod(input1,input2):
    mat = []
    mat.append([0 for i in range(input2+1)])
    for i in range(input1+1):
        mat.append([0 for i in range(input2+1)])
    
    for i in range(input1+1):
        mat[i][0] = 1
    
    for i in range(1,input1+1):
        for j in range(1,input2+1):
            if i < j:
                val = 0
            else:
                val = mat[i-1][j] + mat[i-j][j]%1000000009
            mat[i][j] = val%1000000009
    return mat[input1][input2]%1000000009

def main():
    t = int(input())
    while t:
        input1, input2 = map(int,input().split())
        print(and_tuple_mod(input1,input2))
        t -= 1

if __name__ == '__main__':
    main()