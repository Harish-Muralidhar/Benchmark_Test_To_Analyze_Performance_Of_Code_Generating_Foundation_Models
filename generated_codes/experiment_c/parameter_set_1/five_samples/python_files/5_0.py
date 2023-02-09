'''

Explanation

In the first case the sequence contains the substring 2 3 4 at the index(2).So the answer is "Yes"

In the second case the sequence doesn't contain the substring 4 15. So the answer is "No"

'''

import time
start_time = time.time()

inpt = int(input())

for i in range(inpt):
    seq_len = int(input())
    seq = input().split()
    f_seq_len = int(input())
    f_seq = input().split()
    k = 0
    count = 0
    j = 0
    while k < seq_len:
        if seq[k] == f_seq[j]:
            count += 1
            j += 1
            k += 1
        else:
            k += 1
            j = 0
            count = 0
        if count == f_seq_len:
            print ("Yes")
            break
    if count != f_seq_len:
        print ("No")

print("--- %s seconds ---" % (time.time() - start_time))