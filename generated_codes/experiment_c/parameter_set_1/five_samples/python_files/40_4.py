/*


Explanation
First observer is clearly not from India. The second observer uses the Indian "Yes" gesture in half of his replies (I occurs exactly twice, and N exactly twice), hence we can be sure that he is Indian. The third observer uses the Indian gesture for half of his replies, but there are only 6 replies, so we cannot decide if he is Indian or not.

https://practice.geeksforgeeks.org/problems/detect-indian-or-not/1
*/

def indian_or_not(num_observers):
    for i in range(num_observers):
        observed_number_gestures = input()
        gestures = input()
        number_indian_gestures = gestures.count("I")
        number_non_indian_gestures = gestures.count("Y") + gestures.count("N")
        if number_non_indian_gestures + number_indian_gestures == 0:
            print("NOT SURE")
        elif number_indian_gestures == 0:
            print("NOT INDIAN")
        elif number_non_indian_gestures == 0:
            print("INDIAN")
        else:
            print("NOT SURE")

if __name__ == "__main__":
    num_observers = int(input())
    indian_or_not(num_observers)