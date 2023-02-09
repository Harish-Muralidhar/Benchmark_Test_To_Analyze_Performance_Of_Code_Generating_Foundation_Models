/*
*/

t = int(input());
for i in range(t):
	n = int(input());
	price = list(map(int,input().split()));
	price.sort();
	s = sum(price);
	if(n%2 == 0):
		print(s-price[0]-price[1]);
	else:
		print(s-price[0]);