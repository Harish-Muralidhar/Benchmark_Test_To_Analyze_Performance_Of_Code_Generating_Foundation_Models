

<code>import re

txt = input()
count = 0

for i in range(len(txt)):
    for j in range(i+1, len(txt)+1):
        if len(set(re.findall('[A-Z]', txt[i:j]))) == 3:
            count += 1
print(count)
































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































