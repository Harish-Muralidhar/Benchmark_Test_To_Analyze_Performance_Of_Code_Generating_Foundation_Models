"""


import sys
import time

start_time = time.time()

def main():

    test_case = int(sys.stdin.readline())
    input_string = []
    output_string = []

    for i in range(test_case):
        input_string.append(sys.stdin.readline())

    #print(input_string)

    for i in range(test_case):
        temp = list(input_string[i])
        temp = replace_all(temp)
        temp = replace_all(temp)
        output_string.append(temp)

    print(output_string)

def replace_all(input_string):
    for i in range(len(input_string)-1):
        if (input_string[i]=="(" and input_string[i+1]==")"):
            input_string[i] = ""
            input_string[i+1] = ""
            return input_string
    return input_string

main()
print("--- %s seconds ---" % (time.time() - start_time))

"""