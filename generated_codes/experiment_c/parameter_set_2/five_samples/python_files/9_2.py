'''

Sample Explanation
In the first example, the optimal solution is to remove the letters "CHE" and "F" from the string.

In the second example, the optimal solution is to remove the letters "CH" from the string.

'''

import re

def main():
    S = input()
    print(len(re.findall('(?=CHEF)',S)))

if __name__ == "__main__":
    main()