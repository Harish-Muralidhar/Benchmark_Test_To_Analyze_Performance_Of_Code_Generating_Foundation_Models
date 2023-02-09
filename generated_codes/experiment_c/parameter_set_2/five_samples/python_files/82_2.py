'''


since the number of divisors of 2 is equal to the number of divisors of 5,
the number of divisors of 3 is equal to the number of divisors of 4,
the number of divisors of 1 is equal to the number of divisors of 3,
the number of divisors of 5 is equal to the number of divisors of 2,
the number of divisors of 4 is equal to the number of divisors of 1.

'''

def divisors(n):
    div = []
    for i in range(1,n+1):
        if n%i == 0:
            div.append(i)
    return div

def divisors_count(n):
    return len(divisors(n))

def divisors_list(n):
    return [divisors_count(i) for i in range(1,n+1)]

def divisors_dict(n):
    return {i:divisors_count(i) for i in range(1,n+1)}

def divisors_dict_reverse(n):
    return {divisors_count(i):i for i in range(1,n+1)}

def divisors_dict_reverse_list(n):
    return [divisors_dict_reverse(n)[i] for i in range(1,n+1)]

def divisors_dict_reverse_list_count(n):
    return len(divisors_dict_reverse_list(n))

def divisors_dict_reverse_list_count_mod(n):
    return divisors_dict_reverse_list_count(n)%500009

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(divisors_dict_reverse_list_count_mod(n))

if __name__ == "__main__":
    main()