'''


'''

def run_test(test_cases):
    output = []
    for i in range(test_cases):
        n, m = [int(j) for j in input().split()]
        positions = [int(j) for j in input().split()]
        # positions = [1,2,3,4,5]
        result = []
        for i, position in enumerate(positions):
            temp = []
            for j in range(n):
                if j <= position:
                    temp.append(position-j)
                else:
                    temp.append(j-position)
            result.append(temp)
        output.append(result)
    print(output)
    return(output)

run_test(2)