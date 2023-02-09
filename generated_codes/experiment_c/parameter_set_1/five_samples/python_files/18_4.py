"""

"""

def fact(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact

def zero_cal(num):
    count = 0
    while(num>0):
        r = num%10
        if(r==0):
            count+=1
            num = num/10
        else:
            break
    return count
    
    

def main():
    num = int(input())
    while(num>0):
        value = int(input())
        fac = fact(value)
        zeros = zero_cal(fac)
        print(zeros)
        num-=1


if __name__=="__main__":
    main()