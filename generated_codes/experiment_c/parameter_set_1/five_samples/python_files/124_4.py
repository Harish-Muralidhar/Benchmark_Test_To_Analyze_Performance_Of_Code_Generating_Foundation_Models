"""



Hint

For the first example, the Chef created the appetizers with the numbers 0, 1, 2, and 3. He wrote them on paper in binary as 00, 01, 10, and 11, respectively. He places the paper for the appetizer numbered 0 to the left of the appetizer numbered 0. No server retrieves this appetizer so it is placed in the correct location. He places the paper for the appetizer numbered 1 to the right of the appetizer numbered 1. No server retrieves this appetizer so it is placed in the correct location. He places the paper for the appetizer numbered 2 to the right of the appetizer numbered 2. A server retrieves this appetizer, reads it upside down and places it in location 1. He places the paper for the appetizer numbered 3 to the right of the appetizer numbered 3. A server retrieves this appetizer, reads it upside down and places it in location 0. The appetizers are now arranged in the order [1, 0]. This yields the scrambled message "cehf".

For the second example, the Chef created the appetizers with the numbers 0, 1, 2, 3, 4, 5, 6, and 7. He wrote them on paper in binary as 0000, 0001, 0010, 0011, 0100, 0101, 0110, and 0111, respectively. He places the paper for the appetizer numbered 0 to the left of the appetizer numbered 0. No server retrieves this appetizer so it is placed in the correct location. He places the paper for the appetizer numbered 1 to the right of the appetizer numbered 1. No server retrieves this appetizer so it is placed in the correct location. He places the paper for the appetizer numbered 2 to the right of the appetizer numbered 2. A server retrieves this appetizer, reads it upside down and places it in location 4. He places the paper for the appetizer numbered 3 to the right of the appetizer numbered 3. A server retrieves this appetizer, reads it upside down and places it in location 0. He places the paper for the appetizer numbered 4 to the right of the appetizer numbered 4. A server retrieves this appetizer, reads it upside down and places it in location 5. He places the paper for the appetizer numbered 5 to the right of the appetizer numbered 5. No server retrieves this appetizer so it is placed in the correct location. He places the paper for the appetizer numbered 6 to the right of the appetizer numbered 6. A server retrieves this appetizer, reads it upside down and places it in location 1. He places the paper for the appetizer numbered 7 to the right of the appetizer numbered 7. A server retrieves this appetizer, reads it upside down and places it in location 2. The appetizers are now arranged in the order [5, 1, 2, 0, 4, 3, 6, 7]. This yields the scrambled message "eayejpuinpopolre".

"""

def main():
    test = int(input())
    for _ in range(test):
        length,message = input().split(' ')
        ls = len(message)
        if ls == int(length):
            print(message)
        else:
            for i in range(1,int(length)):
                new = message[2**i-1:] + message[:2**i-1]
                message = new
            print(new)

if __name__ == '__main__':
    main()