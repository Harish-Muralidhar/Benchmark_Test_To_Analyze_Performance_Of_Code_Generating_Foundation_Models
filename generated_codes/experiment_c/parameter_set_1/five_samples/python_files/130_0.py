"""


"""



def main():
    t = int(raw_input())
    for x in range(t):
        a = raw_input()
        count = 0
        i = 0
        while i < len(a) - 1 :
            if a[i] == '.':
                count+=1
                i += int(a[i+1])
            else:
                i+=1
        print count

if __name__ == '__main__':
    main()