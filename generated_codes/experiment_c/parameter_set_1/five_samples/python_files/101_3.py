'''


import sys

class Solution:
    def isCorrect(self,levelCount,levelLeaves):
        if levelCount == 1:
            if levelLeaves[0] == 1:
                return "Yes"
            else:
                return "No"
        else:
            if levelLeaves[levelCount-1] == sum(levelLeaves[:levelCount-1]):
                return self.isCorrect(levelCount-1,levelLeaves)
            else:
                return "No"
                
    def main(self):
        t = int(input())
        for i in range(t):
            n = int(input())
            levelLeaves = list(map(int,input().strip().split()))
            print(self.isCorrect(n,levelLeaves))
        
if __name__ == '__main__':
    Solution().main()

'''


# Solution 2:
class Solution:
    def isCorrect(self,levelCount,levelLeaves):
        if levelCount == 1:
            if levelLeaves[0] == 1:
                return "Yes"
            else:
                return "No"
        else:
            if levelLeaves[levelCount-1] == sum(levelLeaves[:levelCount-1]):
                return self.isCorrect(levelCount-1,levelLeaves)
            else:
                return "No"
                
    def main(self):
        t = int(input())
        for i in range(t):
            n = int(input())
            levelLeaves = list(map(int,input().strip().split()))
            print(self.isCorrect(n,levelLeaves))
        
if __name__ == '__main__':
    Solution().main()