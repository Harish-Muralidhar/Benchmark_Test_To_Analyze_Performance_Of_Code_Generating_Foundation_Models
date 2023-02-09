'''


'''

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def gcd_list(l):
    if len(l)==1:
        return l[0]
    else:
        return gcd(l[0],gcd_list(l[1:]))
    
def get_gcd(l):
    return gcd_list(l)

def get_min_operations(l,k):
    gcd=get_gcd(l)
    if gcd%k==0:
        return 0
    else:
        return (k-gcd%k)
    
def get_min_operations_list(l,k):
    return [get_min_operations(i,k) for i in l]

def get_min_operations_list_for_all_test_cases(l,k):
    return [get_min_operations_list(i,k) for i in l]

def get_min_operations_for_all_test_cases(l,k):
    return [min(i) for i in get_min_operations_list_for_all_test_cases(l,k)]

def get_min_operations_for_all_test_cases_v2(l,k):
    return [min([get_min_operations(i,k) for i in j]) for j in l]

def get_min_operations_for_all_test_cases_v3(l,k):
    return [min([get_min_operations(i,k) for i in j]) for j in l]

def get_min_operations_for_all_test_cases_v4(l,k):
    return [min([get_min_operations(i,k) for i in j]) for j in l]

def get_min_operations_for_all_test_cases_v5(l,k):
    return [min([get_min_operations(i