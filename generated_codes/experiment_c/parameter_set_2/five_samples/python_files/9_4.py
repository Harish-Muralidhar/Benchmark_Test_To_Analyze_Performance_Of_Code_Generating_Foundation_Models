'''

Sample Explanation
In the first sample, the optimal solution is to remove the letters "CHE" and "F" from the string.

In the second sample, the optimal solution is to remove the letters "CHE" from the string.

'''

# Write your code here

def CHEF_in_string(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'C':
            for j in range(i+1, len(s)):
                if s[j] == 'H':
                    for k in range(j+1, len(s)):
                        if s[k] == 'E':
                            for l in range(k+1, len(s)):
                                if s[l] == 'F':
                                    count += 1
    return count

if __name__ == '__main__':
    s = input()
    print(CHEF_in_string(s))