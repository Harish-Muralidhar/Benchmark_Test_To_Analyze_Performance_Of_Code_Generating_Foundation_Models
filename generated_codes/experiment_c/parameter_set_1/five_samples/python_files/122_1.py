'''
'''
def main():
    testcase = int(input())
    while(testcase>0):
        k = int(input())
        if(k==0):
            print("3")
        else:
            result="3."
            for i in range(k):
                result+=str(i)
            print(result)
        testcase-=1
if __name__=='__main__':
    main()