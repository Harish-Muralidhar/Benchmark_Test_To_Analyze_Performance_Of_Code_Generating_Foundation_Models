'''

Solution:
'''

def gcd(a,b):
	if a==0:
		return b
	else:
		return gcd(b%a,a)

def prod_modulo(a):
	prod=1
	for i in range(len(a)):
		prod=(prod*a[i])%1000000007
	return prod

def subset_gcd(arr,n):
	subset=[]
	for i in range(2**n):
		subset_arr=[]
		for j in range(n):
			if((i & (2**j))>0):
				subset_arr.append(arr[j])
		subset.append(subset_arr)
	return subset

def all_subset(arr,n):
	all_subset=[]
	for i in range(n):
		all_subset.append(arr[i])
	return all_subset

def gcd_subsets(subset,n):
	gcd_subsets=[]
	for i in range(2**n):
		if(len(subset[i])>0):
			gcd_subsets.append(gcd(subset[i][0],subset[i][1]))
		else:
			gcd_subsets.append(1)
	return gcd_subsets

def calc_product(arr,n):
	subset=subset_gcd(arr,n)
	all_subset=all_subset(arr,n)
	gcd_subsets=gcd_subsets(subset,n)
	product=prod_modulo(gcd_subsets)
	return product

def main():
	t=int(input())
	while(t>0):
		n=int(input())
		arr=list(map(int,input().split()))
		print(calc_product(arr,n))
		t-=1

if __name__=='__main__':
	main()