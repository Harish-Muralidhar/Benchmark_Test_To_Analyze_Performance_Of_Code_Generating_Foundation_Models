'''

'''




import sys
 
def main():
    testcase=int(input())
    for i in range(testcase):
        n=int(input())
        strr=input()
        strr=strr.split()
        strr=''.join(strr)
        dp=[[0 for i in range(len(strr))] for i in range(len(strr))]
        for i in range(len(strr)):
            dp[i][i]=1
        for i in range(len(strr)-1):
            if(strr[i]==strr[i+1]):
                dp[i][i+1]=1
            else:
                dp[i][i+1]=0
        for k in range(2,len(strr)):
            for i in range(len(strr)-k):
                j=i+k
                if(strr[i]==strr[j]):
                    dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=0
        count=0
        for i in range(len(strr)):
            for j in range(len(strr)):
                if(dp[i][j]==0):
                    count+=1

        print(count)
 
if __name__ == "__main__":
    main()