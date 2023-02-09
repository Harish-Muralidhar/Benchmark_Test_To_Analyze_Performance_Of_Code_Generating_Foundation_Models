"""

Explanation

In the first test case the only such progression is (2, 4, 6). In the second test case there are two such progressions, namely (2, 4, 6) and (2, 5, 7). The first one is lexicographically smaller than the second one, therefore the first two terms of the second progression are 0 0. In the third test case there are four such progressions, namely (1, 9, 17), (5, 13, 21), (9, 17, 25) and (13, 21, 29).

Problem Setter: Shahriar Manzoor
"""
def main():
    """
    Main Function
    """
    test_cases = int(input())
    while test_cases:
        test_cases -= 1
        l_ip = input()
        l_ip = l_ip.split()
        l_ip = list(map(int, l_ip))
        l_ip_left = l_ip[0]
        l_ip_right = l_ip[1]
        l_ip_d = l_ip[2]
        l_ip_n = l_ip[3]
        l_max = 1
        l_max_left = l_max_right = 0
        while l_ip_left <= l_ip_right:
            l_count = 1
            l_temp = l_ip_left
            while l_temp + l_ip_d <= l_ip_right:
                l_temp += l_ip_d
                l_count += 1
            if l_count >= l_max:
                if l_count == l_max:
                    if l_ip_left < l_max_left:
                        l_max_left = l_ip_left
                        l_max_right = l_temp
                else:
                    l_max = l_count
                    l_max_left = l_ip_left
                    l_max_right = l_temp
            l_ip_left += 1
        if l_ip_n > l_max:
            print(l_max, l_max_left, l_max_right)
        else:
            print(0, 0)
if __name__ == "__main__":
    main()