'''


'''
import math
def hamming(x,y):
    count=0;
    for i in range(len(x)):
        if x[i]!=y[i]:
            count+=1
    return count
def main():
    T=int(input())
    while(T>0):
        x=list(input())
        y=list(input())
        count=0
        resz=['']*len(x)
        for i in range(len(x)):
            if x[i]=='W' and y[i]=='W':
                count+=1
                resz[i]='W'
            elif x[i]=='B' and y[i]=='B':
                count+=1
                resz[i]='B'
            else:
                resz[i]='W'
        if count==len(x):
            print(''.join(resz))
        else:
            print(''.join(resz))
        T-=1
if __name__=='__main__':
    main()