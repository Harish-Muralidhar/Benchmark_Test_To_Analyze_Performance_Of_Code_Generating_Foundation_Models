"""

"""

# Write your code here
import sys

def calculate_memory(n, memory):
    memory.sort()
    total_memory = 0
    for i in range(n):
        total_memory += memory[i]
    return total_memory

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        memory = list(map(int, input().split()))
        print(calculate_memory(n, memory))

if __name__ == "__main__":
    main()