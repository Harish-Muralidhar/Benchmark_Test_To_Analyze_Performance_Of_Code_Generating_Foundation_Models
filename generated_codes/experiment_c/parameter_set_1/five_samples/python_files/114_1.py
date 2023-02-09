'''

'''

import sys
gold_plates=list(map(int,input().split()))
N=len(gold_plates)
Min=sys.maxint
Max=0
for i in range(N):
    Min=min(Min,gold_plates[i])
    Max=max(Max,gold_plates[i])
for i in range(1,Max+1):
    gold_plates[i]+=gold_plates[i-1]
for k in range(K+1):
    result=gold_plates[N-1]
    for i in range(1,N):
        if k>=i:
            result=min(result,gold_plates[N-1]-gold_plates[N-i-1]-gold_plates[i]+Min*i)
        else:
            result=min(result,gold_plates[N-1]+Min*k)
    print(result)