"""


Explanation
Example case 1. The first person only knows about "No" gesture, which is used both in India and abroad. The second person uses "Yes" gesture twice, indicating he/she is from India. The third person is from India too, as it is clear from the Indian "Yes" gesture. The last person only knows about "No" gesture, which is used both in India and abroad.

"""

for i in range(int(input())):
    n=int(input())
    s=input()
    if s.count("Y")>0 and s.count("I")==0:
        print("NOT INDIAN")
    elif s.count("N")>0 and s.count("I")==0:
        print("INDIAN")
    else:
        print("NOT SURE")