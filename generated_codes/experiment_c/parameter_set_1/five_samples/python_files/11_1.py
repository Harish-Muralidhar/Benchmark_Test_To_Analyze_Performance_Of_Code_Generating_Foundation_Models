'''
'''
import math

def main():
    p = 4096
    # find the highest 2^i <= p
    i = math.floor(math.log(p, 2))
    print(i)
    # subtract the highest 2^i from p
    p -= 2**i
    print(p)
    # add 1 to count the highest 2^i
    count = 1

    while p > 0:
        # find the highest 2^i <= p
        i = math.floor(math.log(p, 2))
        print(i)
        # subtract the highest 2^i from p
        p -= 2 ** i
        print(p)
        # add 1 to count
        count += 1

    print(count)

if __name__ == '__main__':
    main()