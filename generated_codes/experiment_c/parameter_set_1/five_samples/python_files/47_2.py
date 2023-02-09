'''

Explanation
447474 has 4 occurrences of 4
228 has 0 occurrences of 4
6664 has 1 occurrence of 4
40 has 1 occurrence of 4
81 has 0 occurrences of 4)

Solution

def n_digit_number(n):
    count = 0
    for i in range(n):
        if i % 10 == 4:
            count += 1
            i = i // 10
    return count

num = int(input())
for i in range(num):
    print(n_digit_number(int(input())))

'''


# Question 9

'''
Write a python code for the following question.
Import the necessary libraries.
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

Example 1:
Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.

Constraints:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

Solution

class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = []

    def seat(self) -> int:
        N, students = self.N, self.students
        if not students:
            students.append(0)
            return 0

        # d is the distance to the closest student, i is the student
        # closest to the left of the proposed seat location.
        d, i = students[0], 0
        for a, b in zip(students, students[1:]):
            if (b - a) // 2 > d:
                d, i = (b - a) // 2, a + d
        if N - 1 - students[-1] > d:
            i = N - 1

        bisect.insort(students, i)
        return i

    def leave(self, p: int) -> None:
        self.students.remove(p)

'''


# Question 10

'''
Write a python code for the following question.
Import the necessary libraries.
The series, 1, 3, 6, 10, 15, 21, ... can be considered as a string of 0's and 1's, which is 0110100110010110...

You are given a list of numbers, and the index of the first and last element of the substring of the series you want to find.

You have to find the sum of the series. 

Example

Input:

series = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
start = 3
end = 5

Output: 

36

Explanation: 

The numbers of the series are 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 and the sum of the numbers between 3 and 5 is 1 + 3 + 6 + 10 + 15 = 35.

Constraints

The length of the series array is less than or equal to 10^5.
1 ≤ start ≤ end ≤ length of series

Solution

def n_sum(series, start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += series[i]
    return sum

series = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
start = 3
end = 5
print(n_sum(series, start, end))
'''