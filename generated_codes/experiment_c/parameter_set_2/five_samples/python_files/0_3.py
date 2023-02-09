'''
So, the answer is BWBW.

'''

def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def get_max_hamming_distance(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    if s1_len != s2_len:
        return -1
    else:
        max_hamming_distance = 0
        for i in range(s1_len):
            for j in range(s2_len):
                hamming_distance_value = hamming_distance(s1[i:], s2[j:]) + hamming_distance(s1[:i], s2[:j])
                if hamming_distance_value > max_hamming_distance:
                    max_hamming_distance = hamming_distance_value
                    max_s1_index = i
                    max_s2_index = j
        return max_hamming_distance, max_s1_index, max_s2_index

def get_max_hamming_distance_str(s1, s2):
    max_hamming_distance, max_s1_index, max_s2_index = get_max_hamming_distance(s1, s2)
    return s1[max_s1_index:] + s2[:max_s2_index]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = input()
        s2 = input()
        print(get_max_hamming_distance_str(s1, s2))