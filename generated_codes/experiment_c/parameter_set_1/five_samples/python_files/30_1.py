"""

"""

def is_triangle(a,b,c):
    if (a+b+c == 180):
        return True
    else:
        return False

def main():
    n = int(input())
    for _ in range(n):
        a,b,c = map(int,input().split())
        print("YES") if is_triangle(a,b,c) else print("NO")


if __name__ == '__main__':
    main()