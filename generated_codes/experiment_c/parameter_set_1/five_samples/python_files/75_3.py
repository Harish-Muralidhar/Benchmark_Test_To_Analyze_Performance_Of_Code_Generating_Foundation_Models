"""



Explanation :
Case 1 :
10 can be transformed to 1, 1 to 0.
Case 2 :
1 can be transformed to 0, 2 to 1.
Case 3 :
There is no way to transform any of the numbers to 0.

"""

from io import StringIO
import unittest

def main():
    t = int(input())
    while(t):
        n, k = map(int,input().split())
        arr = list(map(int,input().split()))
        print(func(n, k, arr))
        t -= 1

def func(n, k, arr):
    if(k == 0):
        if(arr.count(0) == n-1):
            return "YES"
        else:
            return "NO"
    arr.sort()
    if(arr[-1] < k):
        return "NO"
    if(arr[-1] == k):
        return "YES"
    if(arr[-1] - k >= k):
        return "NO"
    return "YES"

class Test(unittest.TestCase):
    def test_1(self):
        expected = "YES\nYES\nNO\n"
        out = StringIO()
        main()
        output = out.getvalue().strip()
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()