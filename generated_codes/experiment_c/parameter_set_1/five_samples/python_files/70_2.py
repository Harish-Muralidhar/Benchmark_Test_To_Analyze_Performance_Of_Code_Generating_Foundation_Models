'''

'''

def subset_sum(n, s_value, array):
    s_set = set(s_value)

    array.sort()

    cur_sum = 0

    for i in array:
        temp = cur_sum + i
        if temp in s_set:
            cur_sum = temp
            s_set.remove(temp)
    return array

if __name__ == "__main__":
    test_cases = int(input())
    for test in range(test_cases):
        n = int(input())
        s_value = list(map(int, input().split()))
        array = list(range(n))
        result = subset_sum(n, s_value, array)
        print(" ".join(str(i) for i in result))