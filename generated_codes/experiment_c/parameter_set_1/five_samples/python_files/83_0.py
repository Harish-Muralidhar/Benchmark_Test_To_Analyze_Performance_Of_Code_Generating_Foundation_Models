'''

Explanation
The sample input corresponds to the problem statement.

'''
import sys

lines = sys.stdin.readlines()

N = int(lines[0].split()[0])
sum = 0
sum_list = []
for i in range(1,N+1):
    sum+=int(lines[i].split()[0])
    sum_list.append(sum)
K = int(lines[0].split()[1])
P = int(lines[0].split()[2])

def find_min_partial_sum_mod(sum_list,K,P):
    min_sum = K
    for i in range(0,len(sum_list)):
        mod_sum = sum_list[i]%P
        if mod_sum >=K:
            if mod_sum < min_sum:
                min_sum = mod_sum
                continue
            else:
                continue
        else:
            for j in range(i+1,len(sum_list)):
                seg_sum = sum_list[j]-sum_list[i]
                mod_sum = seg_sum%P
                if mod_sum >=K:
                    if mod_sum < min_sum:
                        min_sum = mod_sum
                    else:
                        continue
                else:
                    continue
    return min_sum

print(find_min_partial_sum_mod(sum_list,K,P))