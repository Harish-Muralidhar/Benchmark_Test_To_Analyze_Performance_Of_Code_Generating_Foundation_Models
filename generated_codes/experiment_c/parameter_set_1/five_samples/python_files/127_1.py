"""
Explanation
Example 1.

Both players can erase the substring "code" in their first turn. However, Teddy can't erase any substring in his turn, so Tracy will win.

Example 2.

Tracy can erase the substring "foo" in her first turn. Since foo is not in the dictionary, Teddy can't do anything and Tracy wins.

Example 3.

Teddy can erase the substring "ssissi" in his first turn. Then Tracy can erase the substring "ppi". Next, Teddy can erase the substring "missi" and Tracy can erase the substring "i". Finally, Teddy can erase the remaining substring "ss" and win.

Note that Tracy can't erase "ssissi" in her first turn because it's not in the dictionary.

"""


def find_substring(s, w):
	if w in s:
		return True
	for i in range(len(w)):
		tmp = w[:i] + w[i+1:]
		if find_substring(s, tmp):
			return True
	return False


def check_winner(s, w):
	tracy = True
	for i in w:
		if find_substring(s, i):
			tracy = not tracy
			s = s.replace(i, "")
	return tracy


t = int(input())
for _ in range(t):
	s = input()
	n = int(input())
	w = []
	for i in range(n):
		w.append(input())
	print("Tracy" if check_winner(s, w) else "Teddy")