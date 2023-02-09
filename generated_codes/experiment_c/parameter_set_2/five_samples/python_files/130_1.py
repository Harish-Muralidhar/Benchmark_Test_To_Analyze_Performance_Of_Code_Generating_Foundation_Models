"""


"""

def main():
    t = int(input())
    for i in range(t):
        n = input()
        n = n.strip()
        n = n.replace("#","")
        n = n.split(".")
        n = [len(i) for i in n]
        print(max(n))

main()