'''
 pairs.
Case 4 : N = 6. Arjuna can make the pair (1,3) and Bhima can make the pair (2,4). Now, Arjuna can make the pair (5,6) and Bhima can not make any further pairs.

'''

def check_winner(n):
    if n%2==0:
        return "Arjuna"
    else:
        return "Bhima"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(check_winner(n))