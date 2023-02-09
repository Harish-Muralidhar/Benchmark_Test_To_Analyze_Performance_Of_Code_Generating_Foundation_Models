'''

'''
def nck(n, r):
    return (fact[n] / (fact[r] * fact[n - r]))
 
if __name__ == "__main__":
     
    #Calculate the factorials till 10^6
    fact = [1] * 1000001
    for i in range(1, 1000001):
        fact[i] = (fact[i - 1] * i) % 1000000007
     
    t = int(input())
     
    for i in range(t):
        n, m = map(int, input().split())
        print(int((nck(n * m, 2) - (nck(n * m - 2, 2) * (n + m - 2) +
                    nck(n * m - 4, 2) * 4)%1000000007)%1000000007))