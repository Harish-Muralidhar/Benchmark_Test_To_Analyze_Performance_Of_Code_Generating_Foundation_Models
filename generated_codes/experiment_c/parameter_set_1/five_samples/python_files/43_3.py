'''
'''

def kitchen():
    number_of_test_cases = int(input("Enter the number of test cases: "))
    for i in range(0,number_of_test_cases):
        number_of_students = int(input("Enter the number of students: "))
        end_time_of_cooking = list(map(int,input("Enter the times when they need to finish cooking (space separated): ").strip().split()))
        time_required_to_cook = list(map(int,input("Enter the time required to cook (space separated): ").strip().split()))
        available_time = 0
        count = 0
        while(count < number_of_students):
            if(available_time >= end_time_of_cooking[count]):
                available_time += time_required_to_cook[count]
                count += 1
            else:
                break
        print(count)
kitchen()