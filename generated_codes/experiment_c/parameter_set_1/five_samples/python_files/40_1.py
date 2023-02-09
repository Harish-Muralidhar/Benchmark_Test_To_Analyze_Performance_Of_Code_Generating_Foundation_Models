'''


Explanation
First person has 2 consecutive "N"s, so he is clearly not from India.Third person has 2 consecutive "Y"s and 2 consecutive "I"s, so he is clearly from India.Second person has 2 consecutive "Y"s, but then he has "NNI", so you cannot be sure whether he is from India or not.

'''

T=int(input())
for i in range(0,T):
    N=int(input())
    s=input()
    if(s.count('Y')>1 or (s.count('N')>1 and s.count('I')>1)):
        print("NOT INDIAN")
    elif(s.count('I')>1 ):
        print("INDIAN")
    else:
        print("NOT SURE")