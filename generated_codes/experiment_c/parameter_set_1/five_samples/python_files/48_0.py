'''

Input:
1
3
1
3
1
Output:
3

Input:
2
5
1
2
3
3
4
3
1
1
1
2
Output:
2
1

Solution:


'''
import operator
def main():
    t=int(input())
    while(t>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        mydict={}
        for i in range(n):
            key=arr[i]
            if(key in mydict):
                mydict[key]+=1
            else:
                mydict[key]=1
        sorted_d = sorted(mydict.items(), key=operator.itemgetter(1))
        print(sorted_d[0][0])
        t-=1
if __name__=="__main__":
    main()