"""

Solution:

"""

import re

def chef_in_string(s):
    count = 0
    while re.search("CHEF", s):
        count += 1
        s = re.sub("CHEF", "", s, 1)
    return count

if __name__ == "__main__":
    s = input()
    print(chef_in_string(s))